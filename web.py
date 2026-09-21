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
    /* ---------- General ---------- */
    .block-container {
        max-width: 1380px;
        padding-top: 2.5rem;
        padding-bottom: 4rem;
    }

    .stApp {
        background: #ffffff;
    }

    /* ---------- Typography ---------- */
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

    /* ---------- Navigation ---------- */
    [data-testid="stSidebarNav"] {
        display: none;
    }

    /* ---------- Project divider ---------- */
    hr {
        margin-top: 3rem;
        margin-bottom: 3rem;
    }

    /* ---------- Small metadata text ---------- */
    .project-meta {
        color: #6b7280;
        font-size: 0.95rem;
        margin-top: -0.35rem;
        margin-bottom: 1.2rem;
    }

    .project-label {
        color: #6b7280;
        font-size: 0.82rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 0.25rem;
    }

    /* ---------- Home intro ---------- */
    .hero-note {
        color: #6b7280;
        font-size: 1rem;
        line-height: 1.7;
    }

    /* ---------- Cards ---------- */
    .category-card {
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 1.2rem;
        height: 100%;
        background: #fafafa;
    }

    .category-number {
        color: #9ca3af;
        font-size: 0.8rem;
        letter-spacing: 0.1em;
        margin-bottom: 0.5rem;
    }

    .category-title {
        font-size: 1.15rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }

    .category-text {
        color: #6b7280;
        line-height: 1.55;
        font-size: 0.92rem;
    }

    /* ---------- Footer ---------- */
    .footer {
        color: #9ca3af;
        font-size: 0.85rem;
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
    "headline": "Urban Design student | University of Architecture of Ho Chi Minh City",
    "pitch": (
        "I work across urban design, spatial thinking and urban analysis, "
        "with an emerging interest in data-driven approaches to urban transformation."
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
#
# "folder": folder inside data/
# "files": file names in display order
#          None = every image in the folder, naturally sorted
# "columns": number of boards/images per row
# "link": external project link, if available
# =====================================================================

PROJECTS = {

    # -----------------------------------------------------------------
    # DESIGN
    # -----------------------------------------------------------------

    "DA_BCKG": {
        "title": "Spatial Composition: Concept Development",
        "meta": "Concept Design Studio | UAH",
        "summary": (
            "An early design exercise focused on spatial composition, "
            "site reading and the relationship between movement, space and form. "
            "The project explores how an initial spatial idea can be developed into a coherent design language."
        ),
        "highlights": [
            "Developed the project from site observation and conceptual thinking.",
            "Explored spatial hierarchy, composition and relationships between different areas.",
            "Translated an abstract concept into drawings, models and architectural representation.",
        ],
        "role": "Individual academic project",
        "tools": "AutoCAD, SketchUp, Adobe Photoshop, Adobe Illustrator",
        "link": "",
        "folder": "DA_BCKG",
        "files": [
            "site-ident-BCKG.pdf",
            "BCKG2.pdf",
            "BCKG3.pdf",
            "BCKG4.pdf",
            "BCKG5.pdf",
        ],
        "columns": 1,
    },

    "TKDT2_DESIGN": {
        "title": "Phan Slip Long",
        "meta": "Urban Design Studio 2 | Urban Design Proposal | UAH",
        "summary": (
            "A neighbourhood-scale urban design proposal in Phan Xích Long, "
            "developed around the everyday relationship between streets, restaurants, "
            "movement and public life. The proposal questions how existing walls and "
            "street edges can be reworked to create places for people to stay, not only pass through."
        ),
        "highlights": [
            "Developed the concept around enhancing existing walls and interrupting visual consistency.",
            "Proposed a linear public layer below ground as an extension of the street experience.",
            "Introduced small public pockets for different forms of lingering, including elderly users, children and teenagers.",
            "Used a central skylight / glass strip to maintain a connection between the underground public space and the street above.",
        ],
        "role": "Individual academic project",
        "tools": "AutoCAD, SketchUp, Adobe Photoshop, Adobe Illustrator",
        "link": "",
        "folder": "TKDT2",
        "files": [
            "3.png",
            "4.png",
            "5.png",
            "6.png",
        ],
        "columns": 1,
    },


    # -----------------------------------------------------------------
    # URBAN ANALYSIS
    # -----------------------------------------------------------------

    "TKDT2_ANALYSIS": {
        "title": "Phan Slip Long: Site Analysis",
        "meta": "Urban Design Studio 2 | Urban Analysis | UAH",
        "summary": (
            "The analysis examines how Phan Xích Long works as an everyday urban environment, "
            "looking beyond physical form to understand how people move, eat, park, gather and leave. "
            "The findings became the basis for the later design intervention."
        ),
        "highlights": [
            "Observed how restaurants generate movement but often do not create places for people to stay.",
            "Identified conflicts between pedestrian activity and sidewalk parking.",
            "Examined street life, mobility, land use and the existing building / façade condition.",
            "Used everyday behaviour as a starting point for identifying public-space opportunities.",
        ],
        "role": "Individual academic project",
        "tools": "Site observation, mapping, AutoCAD, Adobe Photoshop, Adobe Illustrator",
        "link": "",
        "folder": "TKDT2",
        "files": [
            "1.png",
            "2.png",
        ],
        "columns": 1,
    },

    "SALA_GROUP": {
        "title": "Sala: Urban Infrastructure Strategy",
        "meta": "Group Urban Project | Urban Systems & Infrastructure | UAH",
        "summary": (
            "A group study of Sala focused on how infrastructure systems can be integrated "
            "with the urban structure rather than treated as isolated technical networks. "
            "The project explored energy, telecommunications, wastewater, rainwater and mobility as interconnected systems."
        ),
        "highlights": [
            "Developed a ring-based electrical distribution strategy.",
            "Explored rooftop and pond-based solar energy opportunities.",
            "Planned FTTx / central-office allocation as part of the district's digital infrastructure.",
            "Used zoning and grading to support gravity-based wastewater systems.",
            "Integrated rainwater ponds, pocket gardens and bicycle infrastructure into the urban system.",
        ],
        "role": "Group project — contributed to urban infrastructure analysis and system development",
        "tools": "AutoCAD, Adobe Illustrator, Adobe Photoshop, system mapping",
        "link": "",
        "folder": "SALA_GROUP",
        "files": None,
        "columns": 2,
    },

    "TKDT1": {
        "title": "Bến Thành: Transit-Oriented Development",
        "meta": "Urban Design Studio 1 | TOD | UAH",
        "summary": (
            "An academic TOD exercise around Bến Thành Metro Station, "
            "examining the relationship between transit, land use, public space and pedestrian movement. "
            "The project investigates how a major station can connect different urban activities and districts."
        ),
        "highlights": [
            "Studied the pedestrian catchment around Bến Thành Metro Station.",
            "Examined relationships between commercial, residential and office functions.",
            "Investigated pedestrian connections between major urban destinations.",
            "Explored how public space and station access influence the quality of the TOD area.",
        ],
        "role": "Individual academic project",
        "tools": "AutoCAD, SketchUp, Adobe Photoshop, Adobe Illustrator",
        "link": "",
        "folder": "TKDT1",
        "files": [
            "tkdt1-TASK2.png",
            "To 1 BEN THANH.pdf",
            "To 2 Ben Thanh.pdf",
        ],
        "columns": 1,
    },


    # -----------------------------------------------------------------
    # DATA & SUSTAINABILITY
    # -----------------------------------------------------------------

    "AGODA": {
        "title": "Agoda Business Analytics Web App",
        "meta": "Business Analytics | Data Project",
        "summary": (
            "A data analytics project focused on turning a structured business dataset "
            "into an interactive web-based analysis. The project demonstrates the ability "
            "to move from data preparation and exploration to communicating insights through an application."
        ),
        "highlights": [
            "Worked with structured business data and performed exploratory analysis.",
            "Used Python-based data processing and analysis.",
            "Translated analytical results into an interactive web interface.",
            "Focused on communicating patterns and findings clearly rather than only producing charts.",
        ],
        "role": "Individual data project",
        "tools": "Python, pandas, Streamlit",
        "link": "",
        "folder": "AGODA",
        "files": None,
        "columns": 2,
    },

    "EDGE": {
        "title": "EDGE Green Building Assessment",
        "meta": "Green Building Assessment | IFC EDGE",
        "summary": (
            "A building-performance study using the IFC EDGE framework to examine "
            "energy, water and material-related strategies. The project connects architectural "
            "decisions with measurable environmental performance."
        ),
        "highlights": [
            "Evaluated energy-saving strategies and on-site photovoltaic potential.",
            "Studied water-efficiency and wastewater / greywater recovery strategies.",
            "Explored material choices and their relationship with embodied energy.",
            "Used a quantitative performance framework to test design decisions.",
        ],
        "role": "Academic project",
        "tools": "IFC EDGE App, architectural analysis",
        "link": "",
        "folder": "EDGE",
        "files": None,
        "columns": 3,
    },
}


# =====================================================================
# 5. SECTIONS
# =====================================================================

SECTIONS = {
    "Design": {
        "url": "design",
        "intro": (
            "Concept development and spatial design, from site reading to form."
        ),
        "projects": [
            "DA_BCKG",
            "TKDT2_DESIGN",
        ],
    },

    "Urban Analysis": {
        "url": "urban-analysis",
        "intro": (
            "Reading how cities work through streets, mobility, land use, "
            "infrastructure and everyday activity."
        ),
        "projects": [
            "TKDT2_ANALYSIS",
            "SALA_GROUP",
            "TKDT1",
        ],
    },

    "Data & Sustainability": {
        "url": "data-sustainability",
        "intro": (
            "Building an analytical edge through data, quantitative thinking "
            "and environmental performance."
        ),
        "projects": [
            "AGODA",
            "EDGE",
        ],
    },
}


IMAGE_TYPES = {".png", ".jpg", ".jpeg", ".webp"}
PDF_RENDER_WIDTH = 2400


# =====================================================================
# 6. HELPERS
# =====================================================================

def natural_sort_key(file_path: Path):
    """
    Sort files naturally:
    1.png, 2.png, 3.png, ..., 10.png
    instead of
    1.png, 10.png, 2.png
    """
    parts = re.split(r"(\d+)", file_path.name)

    return [
        int(part) if part.isdigit() else part.lower()
        for part in parts
    ]


def get_project_files(project):
    """
    Return the project files in the order defined in PROJECTS.
    If files=None, automatically discover all images in the folder.
    """

    folder = DATA_DIR / project["folder"]

    if not folder.exists():
        return []

    if project["files"] is not None:
        return [
            folder / file_name
            for file_name in project["files"]
        ]

    images = [
        file_path
        for file_path in folder.iterdir()
        if file_path.is_file()
        and file_path.suffix.lower() in IMAGE_TYPES
    ]

    return sorted(images, key=natural_sort_key)


@st.cache_data(show_spinner="Loading drawings...")
def render_pdf_pages(pdf_path_str):
    """
    Render every PDF page into a JPEG.
    Streamlit caches the result so the PDF does not have to
    be rendered again on every interaction.
    """

    page_images = []

    with pymupdf.open(pdf_path_str) as pdf:
        for page in pdf:
            zoom = PDF_RENDER_WIDTH / page.rect.width

            pixmap = page.get_pixmap(
                matrix=pymupdf.Matrix(zoom, zoom)
            )

            page_images.append(
                pixmap.tobytes(
                    "jpeg",
                    jpg_quality=85,
                )
            )

    return page_images


def show_file(file_path: Path):
    """
    Display a single image or PDF.
    """

    if not file_path.exists():
        st.warning(
            f"File not found: {file_path.relative_to(DATA_DIR)}"
        )
        return

    if file_path.suffix.lower() == ".pdf":
        for page_image in render_pdf_pages(str(file_path)):
            st.image(
                page_image,
                width="stretch",
            )

    else:
        st.image(
            str(file_path),
            width="stretch",
        )


def show_files(files, n_columns):
    """
    Display project boards in rows.
    """

    if not files:
        st.info("Project boards will be added here.")
        return

    for row_start in range(0, len(files), n_columns):

        row_files = files[
            row_start:row_start + n_columns
        ]

        columns = st.columns(
            n_columns,
            gap="medium",
        )

        for column, file_path in zip(columns, row_files):

            with column:
                show_file(file_path)


def show_project(project_key):
    """
    Render one complete project.
    """

    project = PROJECTS[project_key]

    st.subheader(project["title"])

    st.markdown(
        f'<div class="project-meta">{project["meta"]}</div>',
        unsafe_allow_html=True,
    )

    text_column, facts_column = st.columns(
        [2.1, 1],
        gap="large",
    )

    with text_column:

        st.write(project["summary"])

        st.markdown("")

        for item in project["highlights"]:
            st.markdown(
                f"- {item}"
            )

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
                use_container_width=True,
            )

    st.markdown("")

    show_files(
        get_project_files(project),
        project["columns"],
    )

    st.divider()


def show_contact():
    """
    Render location, email, LinkedIn and CV download.
    """

    contact_items = [
        PROFILE["location"],
        f"[{PROFILE['email']}](mailto:{PROFILE['email']})",
    ]

    if PROFILE["linkedin"]:
        contact_items.append(
            f"[LinkedIn]({PROFILE['linkedin']})"
        )

    st.markdown(
        " · ".join(contact_items)
    )

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
        f"""
        <div class="footer">
            {PROFILE["name"]} · {PROFILE["email"]} ·
            Built with Python and Streamlit.
        </div>
        """,
        unsafe_allow_html=True,
    )


# =====================================================================
# 7. HOME
# =====================================================================

def show_home():

    text_column, image_column = st.columns(
        [1.15, 1],
        gap="large",
    )

    with text_column:

        st.title(
            PROFILE["name"]
        )

        st.subheader(
            PROFILE["headline"]
        )

        st.markdown("")

        st.markdown(
            f"""
            <div class="hero-note">
                {PROFILE["pitch"]}
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("")

        st.markdown(
            f"**Looking for:** {PROFILE['looking_for']}"
        )

        st.markdown("")

        show_contact()

    with image_column:

        if PROFILE["cover_image"].exists():

            st.image(
                str(PROFILE["cover_image"]),
                width="stretch",
            )

        else:

            st.info(
                "Add the cover image to data/TKDT2/1.png"
            )

    st.divider()

    st.header("Selected Work")

    st.write(
        "A selection of academic work across design, "
        "urban analysis, data and sustainability."
    )

    st.markdown("")

    section_columns = st.columns(
        len(SECTIONS),
        gap="medium",
    )

    for index, (column, (section_name, section)) in enumerate(
        zip(section_columns, SECTIONS.items()),
        start=1,
    ):

        with column:

            st.markdown(
                f"""
                <div class="category-card">
                    <div class="category-number">
                        {index:02d}
                    </div>

                    <div class="category-title">
                        {section_name}
                    </div>

                    <div class="category-text">
                        {section["intro"]}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown("")

            st.page_link(
                SECTION_PAGES[section_name],
                label="View projects",
            )

    st.divider()

    st.header("Approach")

    st.write(
        "My current work sits between urban design and urban analysis, "
        "with a growing interest in how spatial understanding can work "
        "together with data and quantitative methods."
    )

    st.write(
        "The goal is not to replace design thinking with data, "
        "but to use analysis as another way of understanding places, "
        "testing possibilities and supporting urban decision-making."
    )

    st.divider()

    show_footer()


# =====================================================================
# 8. SECTION PAGES
# =====================================================================

def show_section(section_name):

    section = SECTIONS[section_name]

    st.title(section_name)

    st.write(
        section["intro"]
    )

    st.divider()

    for project_key in section["projects"]:
        show_project(project_key)

    show_footer()


# =====================================================================
# 9. NAVIGATION
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

pg = st.navigation(
    [
        home_page,
        *SECTION_PAGES.values(),
    ],
    position="top",
)

pg.run()