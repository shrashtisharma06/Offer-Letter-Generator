import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak
)
from reportlab.lib.units import inch
from datetime import datetime
import os


# ============================================================
# APPLICATION WINDOW
# ============================================================

window = tk.Tk()

window.title("Offer Letter Generator")
window.geometry("1000x850")
window.resizable(False, False)
window.configure(bg="#EAF2F8")


# ============================================================
# GENERATED OFFERS FOLDER
# ============================================================

output_folder = "Generated_Offers"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# ============================================================
# TITLE
# ============================================================

title_label = tk.Label(
    window,
    text="OFFER LETTER GENERATOR",
    font=("Arial", 24, "bold"),
    bg="#1F4E78",
    fg="white",
    pady=15
)

title_label.pack(fill="x")


subtitle_label = tk.Label(
    window,
    text="Create professional employee offer letters in PDF format",
    font=("Arial", 11),
    bg="#EAF2F8",
    fg="#555555"
)

subtitle_label.pack(pady=8)


# ============================================================
# MAIN FRAME
# ============================================================

main_frame = tk.Frame(
    window,
    bg="#EAF2F8"
)

main_frame.pack(fill="both", expand=True, padx=25, pady=5)


# ============================================================
# VARIABLES
# ============================================================

company_name_var = tk.StringVar()
company_address_var = tk.StringVar()
hr_name_var = tk.StringVar()
hr_email_var = tk.StringVar()

employee_name_var = tk.StringVar()
employee_id_var = tk.StringVar()
employee_email_var = tk.StringVar()
employee_phone_var = tk.StringVar()
employee_address_var = tk.StringVar()
designation_var = tk.StringVar()
department_var = tk.StringVar()
joining_date_var = tk.StringVar()
manager_var = tk.StringVar()

annual_ctc_var = tk.StringVar()
monthly_salary_var = tk.StringVar()
basic_salary_var = tk.StringVar()
hra_var = tk.StringVar()
allowance_var = tk.StringVar()
bonus_var = tk.StringVar()


# ============================================================
# COMMON ENTRY FUNCTION
# ============================================================

def create_entry(parent, row, column, label_text, variable):

    label = tk.Label(
        parent,
        text=label_text,
        font=("Arial", 10, "bold"),
        bg="#F8F9F9",
        fg="#333333"
    )

    label.grid(
        row=row,
        column=column,
        padx=8,
        pady=7,
        sticky="w"
    )

    entry = tk.Entry(
        parent,
        textvariable=variable,
        font=("Arial", 10),
        width=27,
        relief="solid",
        bd=1
    )

    entry.grid(
        row=row,
        column=column + 1,
        padx=8,
        pady=7
    )

    return entry


# ============================================================
# COMPANY DETAILS
# ============================================================

company_frame = tk.LabelFrame(
    main_frame,
    text=" COMPANY DETAILS ",
    font=("Arial", 12, "bold"),
    bg="#F8F9F9",
    fg="#1F4E78",
    padx=10,
    pady=10
)

company_frame.grid(
    row=0,
    column=0,
    columnspan=2,
    sticky="ew",
    pady=8
)

create_entry(
    company_frame,
    0,
    0,
    "Company Name",
    company_name_var
)

create_entry(
    company_frame,
    0,
    2,
    "HR Name",
    hr_name_var
)

create_entry(
    company_frame,
    1,
    0,
    "Company Address",
    company_address_var
)

create_entry(
    company_frame,
    1,
    2,
    "HR Email",
    hr_email_var
)


# ============================================================
# EMPLOYEE DETAILS
# ============================================================

employee_frame = tk.LabelFrame(
    main_frame,
    text=" EMPLOYEE DETAILS ",
    font=("Arial", 12, "bold"),
    bg="#F8F9F9",
    fg="#1F4E78",
    padx=10,
    pady=10
)

employee_frame.grid(
    row=1,
    column=0,
    columnspan=2,
    sticky="ew",
    pady=8
)

create_entry(
    employee_frame,
    0,
    0,
    "Employee Name",
    employee_name_var
)

create_entry(
    employee_frame,
    0,
    2,
    "Employee ID",
    employee_id_var
)

create_entry(
    employee_frame,
    1,
    0,
    "Email",
    employee_email_var
)

create_entry(
    employee_frame,
    1,
    2,
    "Phone",
    employee_phone_var
)

create_entry(
    employee_frame,
    2,
    0,
    "Address",
    employee_address_var
)

create_entry(
    employee_frame,
    2,
    2,
    "Designation",
    designation_var
)

create_entry(
    employee_frame,
    3,
    0,
    "Department",
    department_var
)

create_entry(
    employee_frame,
    3,
    2,
    "Joining Date",
    joining_date_var
)

create_entry(
    employee_frame,
    4,
    0,
    "Reporting Manager",
    manager_var
)


# ============================================================
# SALARY DETAILS
# ============================================================

salary_frame = tk.LabelFrame(
    main_frame,
    text=" SALARY DETAILS ",
    font=("Arial", 12, "bold"),
    bg="#F8F9F9",
    fg="#1F4E78",
    padx=10,
    pady=10
)

salary_frame.grid(
    row=2,
    column=0,
    columnspan=2,
    sticky="ew",
    pady=8
)

create_entry(
    salary_frame,
    0,
    0,
    "Annual CTC",
    annual_ctc_var
)

create_entry(
    salary_frame,
    0,
    2,
    "Monthly Salary",
    monthly_salary_var
)

create_entry(
    salary_frame,
    1,
    0,
    "Basic Salary",
    basic_salary_var
)

create_entry(
    salary_frame,
    1,
    2,
    "HRA",
    hra_var
)

create_entry(
    salary_frame,
    2,
    0,
    "Allowances",
    allowance_var
)

create_entry(
    salary_frame,
    2,
    2,
    "Bonus",
    bonus_var
)


# ============================================================
# VALIDATION
# ============================================================

def validate_fields():

    required_fields = [
        (company_name_var.get(), "Company Name"),
        (company_address_var.get(), "Company Address"),
        (hr_name_var.get(), "HR Name"),
        (hr_email_var.get(), "HR Email"),

        (employee_name_var.get(), "Employee Name"),
        (employee_id_var.get(), "Employee ID"),
        (employee_email_var.get(), "Employee Email"),
        (employee_phone_var.get(), "Employee Phone"),
        (employee_address_var.get(), "Employee Address"),
        (designation_var.get(), "Designation"),
        (department_var.get(), "Department"),
        (joining_date_var.get(), "Joining Date"),
        (manager_var.get(), "Reporting Manager"),

        (annual_ctc_var.get(), "Annual CTC"),
        (monthly_salary_var.get(), "Monthly Salary"),
        (basic_salary_var.get(), "Basic Salary"),
        (hra_var.get(), "HRA"),
        (allowance_var.get(), "Allowances"),
        (bonus_var.get(), "Bonus")
    ]

    for value, field_name in required_fields:

        if not value.strip():

            messagebox.showwarning(
                "Missing Information",
                f"Please enter {field_name}."
            )

            return False

    return True


# ============================================================
# PDF GENERATION
# ============================================================

def generate_offer_letter():

    if not validate_fields():
        return

    try:

        # ----------------------------------------------------
        # Get salary values
        # ----------------------------------------------------

        annual_ctc = float(annual_ctc_var.get())
        monthly_salary = float(monthly_salary_var.get())
        basic_salary = float(basic_salary_var.get())
        hra = float(hra_var.get())
        allowance = float(allowance_var.get())
        bonus = float(bonus_var.get())

    except ValueError:

        messagebox.showerror(
            "Invalid Salary",
            "Salary fields must contain numbers only."
        )

        return


    # --------------------------------------------------------
    # Employee name for filename
    # --------------------------------------------------------

    employee_name = employee_name_var.get().strip()

    safe_name = "".join(
        character
        for character in employee_name
        if character.isalnum() or character in (" ", "_", "-")
    )

    safe_name = safe_name.replace(" ", "_")


    # --------------------------------------------------------
    # PDF filename
    # --------------------------------------------------------

    file_name = f"Offer_{safe_name}.pdf"

    file_path = os.path.join(
        output_folder,
        file_name
    )


    # --------------------------------------------------------
    # Create PDF document
    # --------------------------------------------------------

    document = SimpleDocTemplate(
        file_path,
        pagesize=A4,
        rightMargin=50,
        leftMargin=50,
        topMargin=45,
        bottomMargin=45
    )


    # --------------------------------------------------------
    # Styles
    # --------------------------------------------------------

    styles = getSampleStyleSheet()

    company_style = ParagraphStyle(
        "CompanyStyle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=18,
        alignment=TA_CENTER,
        spaceAfter=5
    )

    address_style = ParagraphStyle(
        "AddressStyle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9,
        alignment=TA_CENTER,
        leading=12
    )

    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=16,
        alignment=TA_CENTER,
        spaceBefore=18,
        spaceAfter=20
    )

    normal_style = ParagraphStyle(
        "NormalStyle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10.5,
        leading=17,
        alignment=TA_LEFT
    )

    small_style = ParagraphStyle(
        "SmallStyle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9,
        leading=13
    )


    # --------------------------------------------------------
    # Story
    # --------------------------------------------------------

    story = []


    # --------------------------------------------------------
    # Company Header
    # --------------------------------------------------------

    story.append(
        Paragraph(
            company_name_var.get(),
            company_style
        )
    )

    story.append(
        Paragraph(
            company_address_var.get(),
            address_style
        )
    )

    story.append(Spacer(1, 10))


    # --------------------------------------------------------
    # Horizontal line
    # --------------------------------------------------------

    line_table = Table(
        [[""]],
        colWidths=[7 * inch],
        rowHeights=[2]
    )

    line_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#1F4E78"))
        ])
    )

    story.append(line_table)

    story.append(Spacer(1, 15))


    # --------------------------------------------------------
    # Date and Offer Letter
    # --------------------------------------------------------

    current_date = datetime.now().strftime("%d %B %Y")

    story.append(
        Paragraph(
            f"<b>Date:</b> {current_date}",
            normal_style
        )
    )

    story.append(Spacer(1, 12))

    story.append(
        Paragraph(
            "OFFER OF EMPLOYMENT",
            title_style
        )
    )


    # --------------------------------------------------------
    # Employee Information
    # --------------------------------------------------------

    story.append(
        Paragraph(
            f"Dear <b>{employee_name_var.get()}</b>,",
            normal_style
        )
    )

    story.append(Spacer(1, 10))

    introduction = f"""
    We are pleased to offer you the position of
    <b>{designation_var.get()}</b> in the
    <b>{department_var.get()}</b> department at
    <b>{company_name_var.get()}</b>.
    """

    story.append(
        Paragraph(
            introduction,
            normal_style
        )
    )

    story.append(Spacer(1, 12))


    # --------------------------------------------------------
    # Employee Details Table
    # --------------------------------------------------------

    employee_data = [
        ["Employee ID", employee_id_var.get()],
        ["Email", employee_email_var.get()],
        ["Phone", employee_phone_var.get()],
        ["Designation", designation_var.get()],
        ["Department", department_var.get()],
        ["Joining Date", joining_date_var.get()],
        ["Reporting Manager", manager_var.get()]
    ]

    employee_table = Table(
        employee_data,
        colWidths=[1.8 * inch, 4.9 * inch]
    )

    employee_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#D9EAF7")),
            ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
            ("FONTNAME", (1, 0), (1, -1), "Helvetica"),
            ("FONTSIZE", (0, 0), (-1, -1), 9),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 7),
            ("RIGHTPADDING", (0, 0), (-1, -1), 7),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6)
        ])
    )

    story.append(employee_table)

    story.append(Spacer(1, 18))


    # --------------------------------------------------------
    # Salary Section
    # --------------------------------------------------------

    story.append(
        Paragraph(
            "<b>COMPENSATION DETAILS</b>",
            normal_style
        )
    )

    story.append(Spacer(1, 8))


    salary_data = [
        ["Component", "Amount"],
        ["Annual CTC", f"₹ {annual_ctc:,.2f}"],
        ["Monthly Salary", f"₹ {monthly_salary:,.2f}"],
        ["Basic Salary", f"₹ {basic_salary:,.2f}"],
        ["HRA", f"₹ {hra:,.2f}"],
        ["Allowances", f"₹ {allowance:,.2f}"],
        ["Bonus", f"₹ {bonus:,.2f}"]
    ]

    salary_table = Table(
        salary_data,
        colWidths=[4.3 * inch, 2.4 * inch]
    )

    salary_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1F4E78")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTNAME", (0, 1), (0, -1), "Helvetica-Bold"),
            ("FONTNAME", (1, 1), (1, -1), "Helvetica"),
            ("FONTSIZE", (0, 0), (-1, -1), 9),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ("ALIGN", (1, 1), (1, -1), "RIGHT"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 7),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 7)
        ])
    )

    story.append(salary_table)

    story.append(Spacer(1, 18))


    # --------------------------------------------------------
    # Terms and Conditions
    # --------------------------------------------------------

    story.append(
        Paragraph(
            "<b>TERMS AND CONDITIONS</b>",
            normal_style
        )
    )

    story.append(Spacer(1, 7))


    terms = [
        f"1. Your employment with {company_name_var.get()} will commence on {joining_date_var.get()}.",

        f"2. You will report to {manager_var.get()} or any other person designated by the company.",

        f"3. Your annual Cost to Company (CTC) will be ₹ {annual_ctc:,.2f}.",

        "4. Your compensation is subject to applicable company policies and statutory deductions.",

        "5. You are expected to maintain confidentiality regarding company information, documents, processes and business data.",

        "6. Your employment will be governed by the rules, regulations and policies of the company.",

        "7. The company reserves the right to modify policies and employment terms as permitted by applicable law.",

        "8. You are expected to perform your responsibilities professionally and maintain appropriate workplace conduct."
    ]


    for term in terms:

        story.append(
            Paragraph(
                term,
                normal_style
            )
        )

        story.append(Spacer(1, 5))


    story.append(Spacer(1, 15))


    # --------------------------------------------------------
    # Closing
    # --------------------------------------------------------

    closing = f"""
    We are excited to welcome you to <b>{company_name_var.get()}</b>
    and look forward to your valuable contribution to the organization.
    """

    story.append(
        Paragraph(
            closing,
            normal_style
        )
    )

    story.append(Spacer(1, 25))


    # --------------------------------------------------------
    # Signature Section
    # --------------------------------------------------------

    signature_data = [
        [
            Paragraph(
                f"<b>For {company_name_var.get()}</b>",
                small_style
            ),
            Paragraph(
                "<b>Accepted By</b>",
                small_style
            )
        ],
        [
            "",
            ""
        ],
        [
            Paragraph(
                f"{hr_name_var.get()}<br/>HR Manager<br/>{hr_email_var.get()}",
                small_style
            ),
            Paragraph(
                f"{employee_name_var.get()}<br/>Employee",
                small_style
            )
        ]
    ]


    signature_table = Table(
        signature_data,
        colWidths=[3.4 * inch, 3.4 * inch],
        rowHeights=[25, 35, 50]
    )

    signature_table.setStyle(
        TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LINEABOVE", (0, 2), (0, 2), 0.5, colors.grey),
            ("LINEABOVE", (1, 2), (1, 2), 0.5, colors.grey),
            ("LEFTPADDING", (0, 0), (-1, -1), 5),
            ("RIGHTPADDING", (0, 0), (-1, -1), 5)
        ])
    )

    story.append(signature_table)

    story.append(Spacer(1, 20))


    # --------------------------------------------------------
    # Footer
    # --------------------------------------------------------

    story.append(
        Paragraph(
            "This is a computer-generated offer letter.",
            ParagraphStyle(
                "Footer",
                parent=small_style,
                alignment=TA_CENTER,
                textColor=colors.grey
            )
        )
    )


    # --------------------------------------------------------
    # Build PDF
    # --------------------------------------------------------

    document.build(story)


    # --------------------------------------------------------
    # Success message
    # --------------------------------------------------------

    messagebox.showinfo(
        "Success",
        f"Offer letter generated successfully!\n\nSaved at:\n{os.path.abspath(file_path)}"
    )


# ============================================================
# CLEAR FUNCTION
# ============================================================

def clear_fields():

    variables = [
        company_name_var,
        company_address_var,
        hr_name_var,
        hr_email_var,

        employee_name_var,
        employee_id_var,
        employee_email_var,
        employee_phone_var,
        employee_address_var,
        designation_var,
        department_var,
        joining_date_var,
        manager_var,

        annual_ctc_var,
        monthly_salary_var,
        basic_salary_var,
        hra_var,
        allowance_var,
        bonus_var
    ]

    for variable in variables:
        variable.set("")


# ============================================================
# EXIT FUNCTION
# ============================================================

def exit_application():

    answer = messagebox.askyesno(
        "Exit",
        "Are you sure you want to exit?"
    )

    if answer:
        window.destroy()


# ============================================================
# BUTTON FRAME
# ============================================================

button_frame = tk.Frame(
    main_frame,
    bg="#EAF2F8"
)

button_frame.grid(
    row=3,
    column=0,
    columnspan=2,
    pady=18
)


# ============================================================
# GENERATE BUTTON
# ============================================================

generate_button = tk.Button(
    button_frame,
    text="GENERATE OFFER LETTER",
    font=("Arial", 11, "bold"),
    bg="#1F4E78",
    fg="white",
    activebackground="#163A5A",
    activeforeground="white",
    width=23,
    height=2,
    relief="flat",
    cursor="hand2",
    command=generate_offer_letter
)

generate_button.grid(
    row=0,
    column=0,
    padx=10
)


# ============================================================
# CLEAR BUTTON
# ============================================================

clear_button = tk.Button(
    button_frame,
    text="CLEAR",
    font=("Arial", 11, "bold"),
    bg="#7F8C8D",
    fg="white",
    activebackground="#616A6B",
    activeforeground="white",
    width=12,
    height=2,
    relief="flat",
    cursor="hand2",
    command=clear_fields
)

clear_button.grid(
    row=0,
    column=1,
    padx=10
)


# ============================================================
# EXIT BUTTON
# ============================================================

exit_button = tk.Button(
    button_frame,
    text="EXIT",
    font=("Arial", 11, "bold"),
    bg="#C0392B",
    fg="white",
    activebackground="#922B21",
    activeforeground="white",
    width=12,
    height=2,
    relief="flat",
    cursor="hand2",
    command=exit_application
)

exit_button.grid(
    row=0,
    column=2,
    padx=10
)


# ============================================================
# FOOTER
# ============================================================

footer_label = tk.Label(
    window,
    text="Offer Letter Management System | Python + Tkinter + ReportLab",
    font=("Arial", 9),
    bg="#1F4E78",
    fg="white",
    pady=7
)

footer_label.pack(
    fill="x",
    side="bottom"
)


# ============================================================
# START APPLICATION
# ============================================================

window.mainloop()