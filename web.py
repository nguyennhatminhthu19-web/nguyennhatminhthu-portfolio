
import re
from functools import partial
from pathlib import Path

import pymupdf
import streamlit as st


# =====================================================================
# 1. PAGE CONFIG
# =====================================================================

st.set_page_config(
    page_title="Nguyễn Nhật Minh Thư | Urban Design Portfolio",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# =====================================================================
# 2. GLOBAL STYLING
# =====================================================================

st.markdown(
    """
    <style>
    /* ---------- Base ---------- */
    .stApp {
        background: #ffffff;
        color: #16181d;
    }

    .block-container {
        max-width: 1380px;
        padding-top: 2.25rem;
        padding-bottom: 4rem;
    }

    /* ---------- Force readable text on light background ---------- */
    h1, h2, h3, h4, h5, h6,
    p, li, label,
    [data-testid="stMarkdownContainer"],
    [data-testid="stCaptionContainer"],
    [data-testid="stText"],
    [data-testid="stHeader"] {
        color: #16181d !important;
    }

    [data-testid="stCaptionContainer"] {
        color: #667085 !important;
    }

    a {
        color: #16181d !important;
    }

    /* ---------- Headings ---------- */
    h1, h2, h3 {
        letter-spacing: -0.02em;
    }

    h1 {
        font-size: 3rem !important;
        line-height: 1.05 !important;
    }

    h2 {
        font-size: 2rem !important;
    }

    h3 {
        font-size: 1.35rem !important;
    }

    /* ---------- Project metadata ---------- */
    .project-meta {
        color: #667085 !important;
        font-size: 0.95rem;
        margin-top: -0.35rem;
        margin-bottom: 1.2rem;
    }

    .project-label {
        color: #667085 !important;
        font-size: 0.78rem;
        text-transform: uppercase;
        letter-spacing: 0.09em;
        margin-bottom: 0.25rem;
    }

    /* ---------- Home ---------- */
    .hero-note {
        color: #4b5563 !important;
        font-size: 1rem;
        line-height: 1.7;
    }

    .category-card {
        border: 1px solid #e5e7eb;
        border-radius: 14px;
        padding: 1.25rem;
        height: 100%;
        background: #fafafa;
    }

    .category-number {
        color: #9ca3af !important;
        font-size: 0.8rem;
        letter-spacing: 0.1em;
        margin-bottom: 0.5rem;
    }

    .category-title {
        color: #16181d !important;
        font-size: 1.15rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }

    .category-text {
        color: #667085 !important;
        line-height: 1.55;
        font-size: 0.92rem;
    }

    /* ---------- Project journey ---------- */
    .journey-shell {
        padding: 0.5rem 0 0.75rem 0;
    }

    .journey-stage {
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        perspective: 1400px;
        margin-top: 0.4rem;
        margin-bottom: 0.8rem;
    }

    .journey-caption {
        text-align: center;
        color: #667085 !important;
        font-size: 0.82rem;
        margin-top: 0.35rem;
        margin-bottom: 0.8rem;
    }

    /* Streamlit places the actual image inside this test-id. */
    [data-testid="stImage"] {
        display: flex;
        justify-content: center;
        width: 100%;
    }

    [data-testid="stImage"] img {
        max-width: min(860px, 100%) !important;
        max-height: 70vh;
        width: auto !important;
        height: auto !important;
        object-fit: contain;
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 4px;
        box-shadow:
            0 18px 45px rgba(17, 24, 39, 0.10),
            0 3px 10px rgba(17, 24, 39, 0.05);
        transform-origin: left center;
        backface-visibility: hidden;
        animation: pageFlipIn 0.42s ease-out;
    }

    @keyframes pageFlipIn {
        0% {
            opacity: 0;
            transform: perspective(1400px) rotateY(-18deg) translateX(-18px);
        }
        100% {
            opacity: 1;
            transform: perspective(1400px) rotateY(0deg) translateX(0);
        }
    }

    .journey-progress {
        text-align: center;
        color: #667085 !important;
        font-size: 0.82rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 0.4rem;
    }

    .journey-file {
        text-align: center;
        color: #98a2b3 !important;
        font-size: 0.78rem;
        margin-bottom: 1rem;
        word-break: break-word;
    }

    /* ---------- Buttons ---------- */
    div.stButton > button {
        border-radius: 999px;
        min-height: 2.6rem;
    }

    /* ---------- Footer ---------- */
    .footer {
        color: #98a2b3 !important;
        font-size: 0.82rem;
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# =====================================================================
# 3. PROFILE
# =====================================================================

DATA_DIR = Path(__file__).parent / "data"

PROFILE = {
    "name": "Nguyễn Nhật Minh Thư",
    "headline": "Year 4 Urban Design student | University of Architecture of Ho Chi Minh City (UAH)",
    "pitch": (
        "Strong spatial and design foundation, a clear interest in urban transformation, "
        "and hands-on exposure to data science."
    ),
    "looking_for": "Internship or student position in urban design and planning",
    "location": "Ho Chi Minh City, Vietnam",
    "email": "nguyennhatminhthu19@gmail.com",
    "linkedin": "",
    "cv_file": DATA_DIR / "CV.pdf",
    "cover_image": DATA_DIR / "TKDT2" / "1.png",
}


# =====================================================================
# 4. PROJECTS
# =====================================================================

PROJECTS = {
    "DA_BCKG": {
        "title": "CONCEPT: Đồ Án Bố cục không gian - Spatial Concept project",
        "meta": "Concept design studio | UAH | 2025",
        "summary": "TODO: 2-3 sentences on the site, the problem, and the core concept.",
        "highlights": [
            "TODO: key design move 1",
            "TODO: key design move 2",
            "TODO: key design move 3",
        ],
        "role": "TODO: individual or group of N, and what you did",
        "tools": "TODO: e.g. AutoCAD, SketchUp, Photoshop",
        "link": "",
        "folder": "DA_BCKG",
        "files": [
            "site-ident-BCKG.pdf",
            "BCKG2.pdf",
            "BCKG3.pdf",
            "BCKG4.pdf",
            "BCKG5.pdf",
        ],
    },

    # Phan Xich Long is split into 2 cards so the boards are not repeated.
    "TKDT2_DESIGN": {
        "title": "Phan Xích Long: Urban Design Proposal",
        "meta": "Urban Design Studio 2 | UAH | TODO: year",
        "summary": "TODO: 2-3 sentences on your proposal and the main idea behind it.",
        "highlights": [
            "TODO: design strategy",
            "TODO: key spatial intervention",
            "TODO: what changes for people using the street",
        ],
        "role": "TODO: individual or group of N, and what you did",
        "tools": "TODO",
        "link": "",
        "folder": "TKDT2",
        "files": ["3.png", "4.png", "5.png", "6.png"],
    },

    "TKDT2_ANALYSIS": {
        "title": "Phan Xích Long: Site Analysis",
        "meta": "Urban Design Studio 2 | UAH | TODO: year",
        "summary": "TODO: 2-3 sentences on how the area works today and how it is changing.",
        "highlights": [
            "TODO: finding on street life and activities",
            "TODO: finding on mobility and access",
            "TODO: finding on land use and building fabric",
        ],
        "role": "TODO",
        "tools": "TODO",
        "link": "",
        "folder": "TKDT2",
        "files": ["1.png", "2.png"],
    },

    "SALA_GROUP": {
        "title": "TODO: project title (Sala)",
        "meta": "Urban analysis | Group project | TODO: year",
        "summary": "TODO: 2-3 sentences on what the group studied and what you found.",
        "highlights": [
            "TODO: finding 1",
            "TODO: finding 2",
        ],
        "role": "TODO: group of N, and your part",
        "tools": "TODO",
        "link": "",
        "folder": "SALA_GROUP",
        "files": None,
    },

    "TKDT1": {
        "title": "Transit-Oriented Development at Bến Thành",
        "meta": "Urban Design Studio 1 | TOD | UAH | TODO: year",
        "summary": "TODO: 2-3 sentences on the station area and your TOD approach.",
        "highlights": [
            "TODO: walking catchment around the station",
            "TODO: density and land-use mix",
            "TODO: public space and connections",
        ],
        "role": "TODO",
        "tools": "TODO",
        "link": "",
        "folder": "TKDT1",
        "files": [
            "tkdt1-TASK2.png",
            "BEN_THANH_1.pdf",
            "BEN_THANH_2.pdf",
        ],
    },

    "AGODA": {
        "title": "Agoda Business Analytics Web App",
        "meta": "Business analytics | Data project | TODO: year",
        "summary": "TODO: 2-3 sentences on the question, the data, and what the web app shows.",
        "highlights": [
            "TODO: data source and size",
            "TODO: main analysis",
            "TODO: one key insight",
        ],
        "role": "TODO",
        "tools": "TODO: e.g. Python, pandas, Streamlit",
        "link": "",
        "folder": "AGODA",
        "files": None,
    },

    "EDGE": {
        "title": "EDGE Green Building Assessment",
        "meta": "Green building certification (IFC EDGE) | TODO: year",
        "summary": "TODO: 2-3 sentences on the building and what the EDGE assessment showed.",
        "highlights": [
            "TODO: energy savings vs. base case (%)",
            "TODO: water savings (%)",
            "TODO: embodied energy savings in materials (%)",
        ],
        "role": "TODO",
        "tools": "TODO: e.g. EDGE App",
        "link": "",
        "folder": "EDGE",
        "files": None,
    },
}


# =====================================================================
# 5. SECTIONS
# =====================================================================

SECTIONS = {
    "Design": {
        "url": "design",
        "intro": "Concept development and spatial design, from site reading to form.",
        "projects": ["DA_BCKG", "TKDT2_DESIGN"],
    },
    "Urban Analysis": {
        "url": "urban-analysis",
        "intro": "Reading how cities work: streets, transit, land use, and how places change.",
        "projects": ["TKDT2_ANALYSIS", "SALA_GROUP", "TKDT1"],
    },
    "Data & Sustainability": {
        "url": "data-sustainability",
        "intro": "Tools beyond drawing: data analysis and green building performance.",
        "projects": ["AGODA", "EDGE"],
    },
}


IMAGE_TYPES = {".png", ".jpg", ".jpeg", ".webp"}
PDF_RENDER_WIDTH = 1800


# =====================================================================
# 6. HELPERS
# =====================================================================

def natural_sort_key(file_path):
    """Sort 1.png, 2.png, ..., 10.png naturally."""
    parts = re.split(r"(\d+)", file_path.name)
    return [
        int(part) if part.isdigit() else part.lower()
        for part in parts
    ]


def get_project_files(project):
    """Return explicit project files or all images in its folder."""
    folder = DATA_DIR / project["folder"]

    if project["files"] is not None:
        return [folder / file_name for file_name in project["files"]]

    if not folder.exists():
        return []

    images = [
        file_path
        for file_path in folder.iterdir()
        if file_path.is_file()
        and file_path.suffix.lower() in IMAGE_TYPES
    ]

    return sorted(images, key=natural_sort_key)


@st.cache_data(show_spinner="Loading board...")
def render_pdf_page(pdf_path_str, page_index):
    """Render only the requested PDF page, rather than the whole PDF."""
    with pymupdf.open(pdf_path_str) as pdf:
        if page_index >= len(pdf):
            return None

        page = pdf[page_index]
        zoom = PDF_RENDER_WIDTH / page.rect.width

        pixmap = page.get_pixmap(
            matrix=pymupdf.Matrix(zoom, zoom),
        )

        return pixmap.tobytes(
            "jpeg",
            jpg_quality=88,
        )


@st.cache_data(show_spinner=False)
def get_pdf_page_count(pdf_path_str):
    """Return the number of pages in a PDF."""
    with pymupdf.open(pdf_path_str) as pdf:
        return len(pdf)


def build_journey_items(files):
    """
    Turn project files into a single sequence:
    image -> one item
    PDF -> one item per page
    """

    items = []

    for file_path in files:
        if not file_path.exists():
            items.append(
                {
                    "type": "missing",
                    "path": file_path,
                    "page": None,
                }
            )
            continue

        if file_path.suffix.lower() == ".pdf":
            page_count = get_pdf_page_count(str(file_path))

            for page_index in range(page_count):
                items.append(
                    {
                        "type": "pdf",
                        "path": file_path,
                        "page": page_index,
                    }
                )
        else:
            items.append(
                {
                    "type": "image",
                    "path": file_path,
                    "page": None,
                }
            )

    return items


def show_journey(project_key):
    """
    One-board-at-a-time project journey.
    Previous / Next controls create a book-like page transition.
    """

    project = PROJECTS[project_key]
    files = get_project_files(project)
    items = build_journey_items(files)

    if not items:
        st.info("Project boards will be added here.")
        return

    state_key = f"journey_index_{project_key}"

    if state_key not in st.session_state:
        st.session_state[state_key] = 0

    current_index = st.session_state[state_key]
    total_items = len(items)

    # Keep state safe if files change.
    current_index = max(
        0,
        min(current_index, total_items - 1),
    )
    st.session_state[state_key] = current_index

    current_item = items[current_index]

    st.markdown(
        '<div class="journey-shell">',
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="journey-progress">'
        f'BOARD {current_index + 1:02d} / {total_items:02d}'
        f'</div>',
        unsafe_allow_html=True,
    )

    relative_name = current_item["path"].relative_to(DATA_DIR).as_posix()

    if current_item["type"] == "pdf" and get_pdf_page_count(
        str(current_item["path"])
    ) > 1:
        relative_name += f" · page {current_item['page'] + 1}"

    st.markdown(
        f'<div class="journey-file">{relative_name}</div>',
        unsafe_allow_html=True,
    )

    # Narrow center column -> the board no longer fills the screen.
    left, center, right = st.columns(
        [1.0, 5.8, 1.0],
        gap="medium",
    )

    with left:
        if current_index > 0:
            if st.button(
                "←",
                key=f"prev_{project_key}",
                use_container_width=True,
            ):
                st.session_state[state_key] -= 1
                st.rerun()

    with center:

        if current_item["type"] == "missing":

            st.warning(
                f"File not found: "
                f"{current_item['path'].relative_to(DATA_DIR)}"
            )

        elif current_item["type"] == "pdf":

            image_bytes = render_pdf_page(
                str(current_item["path"]),
                current_item["page"],
            )

            if image_bytes is not None:
                st.image(
                    image_bytes,
                    width="stretch",
                )

        else:

            st.image(
                str(current_item["path"]),
                width="stretch",
            )

    with right:
        if current_index < total_items - 1:
            if st.button(
                "→",
                key=f"next_{project_key}",
                use_container_width=True,
            ):
                st.session_state[state_key] += 1
                st.rerun()

    st.markdown(
        "</div>",
        unsafe_allow_html=True,
    )


def show_project(project_key):
    project = PROJECTS[project_key]

    st.header(project["title"])

    st.markdown(
        f'<div class="project-meta">{project["meta"]}</div>',
        unsafe_allow_html=True,
    )

    text_column, facts_column = st.columns(
        [2, 1],
        gap="large",
    )

    with text_column:
        st.write(project["summary"])

        for item in project["highlights"]:
            st.markdown(f"- {item}")

    with facts_column:

        st.markdown(
            '<div class="project-label">Role</div>',
            unsafe_allow_html=True,
        )
        st.write(project["role"])

        st.markdown(
            '<div class="project-label">Tools</div>',
            unsafe_allow_html=True,
        )
        st.write(project["tools"])

        if project["link"]:
            st.link_button(
                "Open project",
                project["link"],
            )

    show_journey(project_key)

    st.divider()


def show_contact():
    contact = (
        f"{PROFILE['location']} · "
        f"[{PROFILE['email']}](mailto:{PROFILE['email']})"
    )

    if PROFILE["linkedin"]:
        contact += f" · [LinkedIn]({PROFILE['linkedin']})"

    st.markdown(contact)

    cv_file = PROFILE["cv_file"]

    if cv_file.exists():
        st.download_button(
            "Download CV",
            data=cv_file.read_bytes(),
            file_name=cv_file.name,
            mime="application/pdf",
        )


def show_footer():
    st.markdown(
        f'<div class="footer">'
        f'{PROFILE["name"]} · {PROFILE["email"]} · '
        f'This site is built with Python and Streamlit.'
        f'</div>',
        unsafe_allow_html=True,
    )


# =====================================================================
# 7. PAGES
# =====================================================================

def show_home():

    text_column, image_column = st.columns(
        [1, 1],
        gap="large",
    )

    with text_column:

        st.title(PROFILE["name"])
        st.subheader(PROFILE["headline"])
        st.write(PROFILE["pitch"])
        st.markdown(
            f"**Looking for:** {PROFILE['looking_for']}"
        )
        show_contact()

    with image_column:

        if PROFILE["cover_image"].exists():
            st.image(
                str(PROFILE["cover_image"]),
                width="stretch",
            )

    st.divider()

    for column, (section_name, section) in zip(
        st.columns(len(SECTIONS)),
        SECTIONS.items(),
    ):

        with column:

            st.subheader(section_name)
            st.caption(section["intro"])

            for project_key in section["projects"]:
                st.markdown(
                    f"- {PROJECTS[project_key]['title']}"
                )

            st.page_link(
                SECTION_PAGES[section_name],
                label="View projects",
            )

    st.divider()

    show_footer()


def show_section(section_name):

    section = SECTIONS[section_name]

    st.title(section_name)
    st.write(section["intro"])
    st.divider()

    for project_key in section["projects"]:
        show_project(project_key)

    show_footer()


# =====================================================================
# 8. NAVIGATION
# =====================================================================

SECTION_PAGES = {
    section_name: st.Page(
        partial(
            show_section,
            section_name,
        ),
        title=section_name,
        url_path=section["url"],
    )
    for section_name, section in SECTIONS.items()
}

home_page = st.Page(
    show_home,
    title="Home",
    default=True,
)

st.navigation(
    [
        home_page,
        *SECTION_PAGES.values(),
    ],
    position="top",
).run()