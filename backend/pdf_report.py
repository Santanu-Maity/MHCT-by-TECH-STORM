from io import BytesIO

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph
)

from database import get_connection


def generate_pdf(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            created_at,
            mental_state,
            mental_score,
            anxiety_score,
            depression_score,
            risk_level
        FROM assessments
        WHERE user_id=?
        ORDER BY created_at DESC
    """, (user_id,))

    rows = cursor.fetchall()

    conn.close()

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph("<b>MindCare AI Assessment Report</b>", styles["Title"])
    )

    elements.append(
        Paragraph("<br/>", styles["Normal"])
    )

    table_data = [[
        "Date",
        "Mental State",
        "Mental",
        "Anxiety",
        "Depression",
        "Risk"
    ]]

    for row in rows:

        table_data.append([
            str(row["created_at"]),
            row["mental_state"],
            str(row["mental_score"]),
            str(row["anxiety_score"]),
            str(row["depression_score"]),
            row["risk_level"]
        ])

    table = Table(table_data)

    table.setStyle(TableStyle([

        ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),

        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

        ("GRID", (0, 0), (-1, -1), 1, colors.black),

        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),

        ("ALIGN", (0, 0), (-1, -1), "CENTER"),

        ("BOTTOMPADDING", (0, 0), (-1, 0), 10)

    ]))

    elements.append(table)

    doc.build(elements)

    buffer.seek(0)

    return buffer