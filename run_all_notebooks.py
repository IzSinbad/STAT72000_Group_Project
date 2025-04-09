"""
Music Success Analysis - Main Runner Script

This script runs all the notebooks in sequence, allowing for a complete analysis
without having to manually open and run each notebook.

This version uses nbformat and nbclient directly instead of calling Jupyter commands,
making it more portable across different environments.

Usage:
    python run_all_notebooks.py
"""

import os
import sys
import time
import traceback
import nbformat
from nbclient import NotebookClient

def print_header(message):
    """Print a formatted header message."""
    print("\n" + "=" * 80)
    print(f" {message} ".center(80, "="))
    print("=" * 80 + "\n")

def run_notebook(notebook_path):
    """Run a Jupyter notebook using nbformat and nbclient."""
    print_header(f"Running {os.path.basename(notebook_path)}")
    
    try:
        # Load the notebook
        print(f"Loading notebook: {notebook_path}")
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        
        # Execute the notebook
        print(f"Executing notebook...")
        client = NotebookClient(
            nb, 
            timeout=600,  # 10-minute timeout
            kernel_name='python3',
            resources={'metadata': {'path': os.path.dirname(os.path.abspath(notebook_path))}}
        )
        
        # Execute and capture output
        client.execute()
        
        # Save the executed notebook
        print(f"Saving executed notebook...")
        with open(notebook_path, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        
        print(f"\n✅ Successfully executed {os.path.basename(notebook_path)}")
        return True
            
    except Exception as e:
        print(f"\n❌ Error executing {os.path.basename(notebook_path)}")
        print(f"Exception: {str(e)}")
        traceback.print_exc()
        return False

def check_dependencies():
    """Check if required dependencies are installed."""
    try:
        import nbformat
        import nbclient
        return True
    except ImportError as e:
        print(f"❌ Error: Missing required dependencies: {str(e)}")
        print("Please install required packages with: pip install nbformat nbclient")
        return False

def main():
    """Main function to run all notebooks in sequence."""
    print_header("Music Success Analysis - Running All Notebooks")
    
    # Check dependencies
    if not check_dependencies():
        return
    
    # List of notebooks to run in order
    notebooks = [
        "1_Data_Loading_Cleaning.ipynb",
        "2_Statistical_Analysis.ipynb",
        "3_Platform_Comparisons.ipynb",
        "4_Artist_Playlist_Analysis.ipynb",
        "5_Explicit_Content_Analysis.ipynb"
    ]
    
    # Track start time
    start_time = time.time()
    
    # Run each notebook in sequence
    success_count = 0
    for notebook in notebooks:
        if run_notebook(notebook):
            success_count += 1
        else:
            print(f"\n⚠️ Warning: Continuing to next notebook despite error in {notebook}")
    
    # Calculate elapsed time
    elapsed_time = time.time() - start_time
    minutes, seconds = divmod(elapsed_time, 60)
    
    # Print summary
    print_header("Execution Summary")
    print(f"Total notebooks: {len(notebooks)}")
    print(f"Successfully executed: {success_count}")
    print(f"Failed: {len(notebooks) - success_count}")
    print(f"Total execution time: {int(minutes)} minutes, {int(seconds)} seconds")
    
    if success_count == len(notebooks):
        print("\n🎉 All notebooks executed successfully!")
    else:
        print("\n⚠️ Some notebooks failed to execute. Check the output above for details.")

if __name__ == "__main__":
    main()
