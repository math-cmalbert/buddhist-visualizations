import os
import sys
from datetime import datetime

def create_principle(principle_name, tibetan="", sanskrit=""):
    """Create a new principle with required files and structure."""
    
    # Create principle directory
    principle_dir = f"principles/{principle_name.lower().replace(' ', '-')}"
    os.makedirs(principle_dir, exist_ok=True)
    
    # Read template
    with open('templates/principle-template.md', 'r') as f:
        template = f.read()
    
    # Replace placeholders
    content = template.replace('[Principle Name]', principle_name)
    content = content.replace('[Tibetan]', tibetan)
    content = content.replace('[Sanskrit]', sanskrit)
    
    # Create README.md
    with open(f"{principle_dir}/README.md", 'w') as f:
        f.write(content)
    
    # Create visualization directory
    viz_dir = f"visualizations/{principle_name.lower().replace(' ', '-')}"
    os.makedirs(viz_dir, exist_ok=True)
    
    print(f"Created principle structure for: {principle_name}")
    print(f"- Principle documentation: {principle_dir}/README.md")
    print(f"- Visualization directory: {viz_dir}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python create_principle.py 'Principle Name' '[Tibetan]' '[Sanskrit]'")
        sys.exit(1)
    
    principle_name = sys.argv[1]
    tibetan = sys.argv[2] if len(sys.argv) > 2 else ""
    sanskrit = sys.argv[3] if len(sys.argv) > 3 else ""
    
    create_principle(principle_name, tibetan, sanskrit)