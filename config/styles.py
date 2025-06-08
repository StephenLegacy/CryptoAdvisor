# Custom CSS for the application
MAIN_STYLE = """
<style>
    .stApp {
        background: linear-gradient(135deg, #1e1e2f 0%, #2d2d44 100%);
        color: #ffffff;
    }
    .stTextInput>div>div>input {
        background-color: #2d2d44;
        color: white;
        border: 1px solid #4a4a6a;
    }
    .stButton>button {
        background: linear-gradient(90deg, #6e45e2 0%, #88d3ce 100%);
        color: white;
        border: none;
        border-radius: 20px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #88d3ce 0%, #6e45e2 100%);
    }
    /* ... (other styles from original) */
</style>
"""

SIDEBAR_STYLE = """
<style>
    .sidebar .sidebar-content {
        background: #2d2d44;
    }
    /* ... (sidebar specific styles) */
</style>
"""

def apply_styles():
    """Apply all custom styles"""
    return MAIN_STYLE + SIDEBAR_STYLE
