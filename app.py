import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="The Legend of Harish",
    page_icon="🎨",
    layout="wide",
)

# 2. Inject Custom CSS for Premium Museum Aesthetics
st.markdown(
    """
    <style>
        /* Main Container Styling overrides */
        .stApp {
            background-color: #1a1a24;
            color: #f5f5f7;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        /* Custom Header Styling */
        .museum-header {
            background: linear-gradient(135deg, #ff6b6b 0%, #4ecdc4 100%);
            padding: 3rem 2rem;
            text-align: center;
            border-radius: 16px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 20px rgba(0,0,0,0.4);
        }
        .museum-header h1 {
            margin: 0;
            font-size: 2.8rem;
            color: #ffffff;
            letter-spacing: 3px;
            text-shadow: 3px 3px 0px #1a1a24;
            text-transform: uppercase;
        }
        .museum-header p {
            margin: 1rem 0 0 0;
            color: #ffffff;
            font-size: 1.2rem;
            font-weight: bold;
            background: rgba(0, 0, 0, 0.2);
            display: inline-block;
            padding: 0.5rem 1.5rem;
            border-radius: 50px;
        }
        
        /* Section Headings */
        .section-title {
            color: #ff6b6b;
            font-size: 1.8rem;
            border-bottom: 3px solid #4ecdc4;
            padding-bottom: 0.5rem;
            text-transform: uppercase;
            margin-top: 1rem;
            margin-bottom: 1.5rem;
        }
        
        /* Gallery Card Structure */
        .gallery-card {
            background-color: #252538;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 6px 12px rgba(0,0,0,0.2);
            border: 2px solid #383852;
            padding: 0px;
            margin-bottom: 1.5rem;
            transition: all 0.3s ease;
        }
        .gallery-card:hover {
            transform: translateY(-5px);
            border-color: #ff6b6b;
        }
        .caption-box {
            padding: 1.2rem;
        }
        .img-tag {
            font-size: 0.75rem;
            text-transform: uppercase;
            background: #4ecdc4;
            color: #1a1a24;
            padding: 0.2rem 0.6rem;
            border-radius: 4px;
            font-weight: bold;
            display: inline-block;
            margin-bottom: 0.5rem;
        }
        .desc {
            font-size: 0.95rem;
            line-height: 1.5;
            color: #e0e0e6;
        }
        
        /* Footer Layout */
        .museum-footer {
            text-align: center;
            padding: 2rem;
            color: #a0a0b0;
            font-size: 0.95rem;
            background-color: #12121a;
            border-top: 2px solid #252538;
            border-radius: 8px;
            margin-top: 3rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# 3. Header Title Block
st.markdown(
    """
    <div class="museum-header">
        <h1>The Harish Exhibition</h1>
        <p>An Unauthorized Digital Museum</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# 4. Media Section: Rare Video Footage
st.markdown('<div class="section-title">Rare Video Footage</div>', unsafe_allow_html=True)

# Using native Streamlit video element centered via columns
v_col1, v_col2, v_col3 = st.columns([1, 3, 1])
with v_col2:
    try:
        st.video("video1.mp4")
    except Exception:
        st.info("Place your 'video1.mp4' file in the root directory to preview the video.")

st.markdown("<br>", unsafe_allow_html=True)

# 5. Media Section: Photographic Gallery Data Structure
st.markdown('<div class="section-title">The Photographic Archives (17 Dossiers)</div>', unsafe_allow_html=True)

# Define your exhibition data list (easily expandable up to all 17 items)
gallery_items = [
    {
        "img": "harish1.jpg",
        "tag": "Evidence #01",
        "desc": "Harish trying to look deep and philosophical, but actually just trying to calculate if he left the stove on."
    },
    {
        "img": "harish2.jpg",
        "tag": "Evidence #02",
        "desc": "The exact facial expression he makes right before telling a joke that absolutely nobody requested to hear."
    },
    {
        "img": "harish3.jpg",
        "tag": "Evidence #03",
        "desc": "Staring intensely at his phone screen like he's debugging production code, but he's just playing Subway Surfers."
    }
]

# Generate a responsive 3-column layout grid dynamically
cols = st.columns(3)

for index, item in enumerate(gallery_items):
    # Distribute elements evenly across columns using modulation rule math
    with cols[index % 3]:
        # Wrap image rendering and text captions securely inside custom CSS cards
        st.markdown('<div class="gallery-card">', unsafe_allow_html=True)
        try:
            st.image(item["img"], use_container_width=True)
        except Exception:
            # Fallback if image isn't uploaded to server local environment yet
            st.warning(f"Missing {item['img']}")
            
        st.markdown(
            f"""
            <div class="caption-box">
                <span class="img-tag">{item['tag']}</span>
                <div class="desc">{item['desc']}</div>
            </div>
            </div>
            """, 
            unsafe_allow_html=True
        )

# 6. Footer Content Block
st.markdown(
    """
    <div class="museum-footer">
        Maintained securely on AWS EC2 by an anonymous friend. All rights to roast reserved.
    </div>
    """,
    unsafe_allow_html=True,
)
