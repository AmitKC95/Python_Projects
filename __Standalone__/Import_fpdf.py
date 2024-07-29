from fpdf import FPDF

# Sample text from conversation
text = """
Here are some helpful commands you can use:
1. `ipconfig`: Display network configuration.
2. `ping [address]`: Test connectivity to a network address.
3. `chkdsk`: Check disk for errors.
4. `sfc /scannow`: Scan system files for integrity issues.
5. `tasklist`: List all running tasks.
"""

# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", size=12)

# Add a cell
pdf.cell(200, 10, txt="ChatGPT Conversation", ln=True, align='C')

# Add multiline text
pdf.multi_cell(0, 10, text)

# Save the PDF with name .pdf
pdf.output("ChatGPT_Conversation.pdf")
