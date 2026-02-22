import os
import json
import subprocess
import sys
from pathlib import Path
from typing import Optional, Dict, Any, List
import importlib.util

class StoryDiffusionComicsAPI:
    def __init__(self):
        self.extension_dir = Path(__file__).parent.parent
        self.models_dir = self.extension_dir / "models"
        self.models_dir.mkdir(exist_ok=True)
        self.current_model = None
        self.available_models = self._scan_models()
        self.sd_module = None
        
    def _scan_models(self) -> List[str]:
        """Scan available StoryDiffusion Comics models"""
        models = []
        if self.models_dir.exists():
            for model_dir in self.models_dir.iterdir():
                if model_dir.is_dir():
                    models.append(model_dir.name)
        return models
    
    def load_model(self, model_name: str) -> bool:
        """Load a specific StoryDiffusion Comics model"""
        try:
            model_path = self.models_dir / model_name
            if not model_path.exists():
                return False
            self.current_model = model_name
            return True
        except Exception as e:
            print(f"Error loading model {model_name}: {e}")
            return False
    
    def generate_comic(
        self,
        prompt: str,
        comic_style: str = "cartoon",
        num_panels: int = 4,
        panel_size: str = "512x512",
        num_inference_steps: int = 25,
        guidance_scale: float = 7.5,
        seed: int = -1,
        negative_prompt: str = "",
        **kwargs
    ) -> Dict[str, Any]:
        """Generate a comic strip using StoryDiffusion Comics"""
        
        if not self.current_model:
            return {
                "success": False,
                "error": "No model loaded. Please load a model first."
            }
        
        try:
            # Prepare generation parameters
            params = {
                "prompt": prompt,
                "negative_prompt": negative_prompt,
                "comic_style": comic_style,
                "num_panels": num_panels,
                "panel_size": panel_size,
                "num_inference_steps": num_inference_steps,
                "guidance_scale": guidance_scale,
                "seed": seed if seed >= 0 else -1,
                "model_name": self.current_model
            }
            
            # Merge any additional kwargs
            params.update(kwargs)
            
            # Call StoryDiffusion Comics generation
            result = self._call_story_diffusion(params)
            
            return {
                "success": True,
                "images": result.get("images", []),
                "info": result.get("info", {}),
                "parameters": params
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def _call_story_diffusion(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Internal method to call StoryDiffusion Comics pipeline"""
        # This will be integrated with the actual StoryDiffusion Comics library
        # For now, returning a template structure
        
        try:
            # Try to import and use StoryDiffusion if available
            from diffusers import DiffusionPipeline
            import torch
            
            model_name = params["model_name"]
            model_path = self.models_dir / model_name
            
            # Load the model (placeholder - adjust based on actual StoryDiffusion setup)
            # pipeline = DiffusionPipeline.from_pretrained(str(model_path))
            
            # For now, return placeholder
            return {
                "images": [],
                "info": {
                    "model": model_name,
                    "style": params["comic_style"],
                    "panels": params["num_panels"]
                }
            }
        except ImportError:
            return {
                "images": [],
                "info": {"warning": "StoryDiffusion not installed. Please install dependencies."}
            }
    
    def get_models(self) -> List[str]:
        """Get list of available models"""
        self.available_models = self._scan_models()
        return self.available_models
    
    def get_comic_styles(self) -> List[str]:
        """Get available comic styles"""
        return [
            "cartoon",
            "manga",
            "comic_book",
            "graphic_novel",
            "watercolor",
            "oil_painting",
            "sketch"
        ]
    
    def get_panel_sizes(self) -> List[str]:
        """Get available panel sizes"""
        return [
            "256x256",
            "512x512",
            "768x768",
            "1024x1024"
        ]
    
    def unload_model(self) -> None:
        """Unload current model"""
        self.current_model = None

# Global API instance
_story_diffusion_api = None

def get_sd_api() -> StoryDiffusionComicsAPI:
    """Get or create the StoryDiffusion Comics API instance"""
    global _story_diffusion_api
    if _story_diffusion_api is None:
        _story_diffusion_api = StoryDiffusionComicsAPI()
    return _story_diffusion_api
