import random

def generate_quadratic_problem(difficulty='easy'):
    if difficulty == 'easy':
        # Coefficients for ax^2 + bx + c, where a = 1
        a = 1
        c = random.randint(1, 10)  # Choose c such that it's easy to factor
        # b is the sum of the roots, which should be easy to calculate for factoring
        factors = [i for i in range(-c, c+1) if i and c % i == 0]
        b = sum(random.sample(factors, 2))
        
    elif difficulty == 'medium':
        # Varying a, not necessarily 1
        a = random.randint(2, 5)
        c = random.randint(1, 10)
        factors = [i for i in range(-c * a, c * a + 1) if i and (c * a) % i == 0]
        b = sum(random.sample(factors, 2)) // a
        
    else:  # hard
        # Use larger coefficients
        a = random.randint(2, 10)
        c = random.randint(1, 50)
        factors = [i for i in range(-c * a, c * a + 1) if i and (c * a) % i == 0]
        b = sum(random.sample(factors, 2)) // a
    
    if b == 0:
        return f"{a}x^2 + {c}"
    else:
        return f"{a}x^2 + {b}x + {c}"


from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Quadratic Factoring Problems', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

# Generate 10 mixed difficulty problems
problems = [generate_quadratic_problem(random.choice(['easy', 'medium', 'hard'])) for _ in range(10)]

def format_quadratic_for_pdf(expression):
    """
    Formats the quadratic expression with superscripts for the PDF.
    """
    formatted_expression = ""
    parts = expression.split(" ")
    for part in parts:
        if "x^2" in part:
            formatted_expression += "x² "  # Superscript 2 for squared terms
        elif "x" in part:
            formatted_expression += part.replace("x", "x ")  # Add space for consistency
        else:
            formatted_expression += part + " "  # Add space for consistency
    return formatted_expression.strip()

# Create a new PDF document with formatted problems
pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.chapter_title('Practice Problems (Formatted)')

# Add formatted problems to the PDF
for i, problem in enumerate(problems, start=1):
    formatted_problem = format_quadratic_for_pdf(problem)
    pdf.chapter_body(f'Problem {i}: Factor. {formatted_problem}')

# Save the new PDF to a file
pdf_file_path_formatted = 'YOUR FILE PATH HERE/quadratic_problems_formatted.pdf'
pdf.output(pdf_file_path_formatted)

