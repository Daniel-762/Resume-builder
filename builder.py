import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext
from fpdf import FPDF
import random
from datetime import datetime

class ProfessionalResumeBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("Professional Resume Builder 2025")
        self.root.geometry("1100x750")
        self.root.configure(bg='#1e3a8a')
        
        # Blue color theme
        self.colors = {
            'primary': '#1e3a8a',
            'secondary': '#3b82f6',
            'accent': '#60a5fa',
            'light_bg': '#dbeafe',
            'card_bg': '#ffffff'
        }
        
        # Real industry facts and statistics
        self.industry_facts = {
            'technology': {
                'skills': ['Python', 'JavaScript', 'Cloud Computing', 'Agile Methodology', 'DevOps', 'Machine Learning'],
                'metrics': {'avg_salary': '$112,000', 'growth_rate': '13%', 'demand': 'High'}
            },
            'healthcare': {
                'skills': ['Patient Care', 'Medical Terminology', 'HIPAA Compliance', 'Electronic Health Records', 'Clinical Research'],
                'metrics': {'avg_salary': '$68,000', 'growth_rate': '16%', 'demand': 'Very High'}
            },
            'finance': {
                'skills': ['Financial Analysis', 'Excel', 'Risk Management', 'Accounting', 'Data Analysis'],
                'metrics': {'avg_salary': '$78,000', 'growth_rate': '7%', 'demand': 'Stable'}
            },
            'marketing': {
                'skills': ['Digital Marketing', 'SEO', 'Social Media', 'Content Creation', 'Analytics'],
                'metrics': {'avg_salary': '$65,000', 'growth_rate': '10%', 'demand': 'High'}
            },
            'education': {
                'skills': ['Curriculum Development', 'Student Assessment', 'Classroom Management', 'Educational Technology'],
                'metrics': {'avg_salary': '$52,000', 'growth_rate': '5%', 'demand': 'Stable'}
            }
        }
        
        # Real company examples
        self.real_companies = {
            'technology': ['Google', 'Microsoft', 'Apple', 'Amazon', 'Meta', 'Netflix', 'Tesla'],
            'healthcare': ['Mayo Clinic', 'Cleveland Clinic', 'Kaiser Permanente', 'UnitedHealth', 'Johnson & Johnson'],
            'finance': ['JPMorgan Chase', 'Goldman Sachs', 'Morgan Stanley', 'Bank of America', 'Wells Fargo'],
            'marketing': ['Procter & Gamble', 'Omnicom', 'WPP', 'Publicis', 'Interpublic'],
            'education': ['Harvard University', 'Stanford University', 'MIT', 'University of Michigan', 'NYU']
        }
        
        self.create_interface()
    
    def create_interface(self):
        # Header with blue background
        header = tk.Frame(self.root, bg=self.colors['primary'], height=80)
        header.pack(fill='x', padx=0, pady=0)
        header.pack_propagate(False)
        
        title = tk.Label(header, text="Professional Resume Builder 2025", 
                        font=('Arial', 20, 'bold'), 
                        fg='white', bg=self.colors['primary'])
        title.pack(pady=20)
        
        # Main container
        main_container = tk.Frame(self.root, bg=self.colors['light_bg'])
        main_container.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Notebook
        self.notebook = ttk.Notebook(main_container)
        self.notebook.pack(fill='both', expand=True)
        
        # Create tabs
        self.input_tab = tk.Frame(self.notebook, bg=self.colors['light_bg'])
        self.preview_tab = tk.Frame(self.notebook, bg=self.colors['light_bg'])
        
        self.notebook.add(self.input_tab, text="📝 Enter Your Details")
        self.notebook.add(self.preview_tab, text="👁️ Preview Resume")
        
        self.create_input_tab()
        self.create_preview_tab()
    
    def create_input_tab(self):
        # Input container with scrollbar
        input_container = tk.Frame(self.input_tab, bg=self.colors['light_bg'])
        input_container.pack(fill='both', expand=True)
        
        # Canvas and scrollbar
        canvas = tk.Canvas(input_container, bg=self.colors['light_bg'], highlightthickness=0)
        scrollbar = ttk.Scrollbar(input_container, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.colors['light_bg'])
        
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Personal Information Card
        personal_card = tk.Frame(scrollable_frame, bg=self.colors['card_bg'], relief='raised', bd=2)
        personal_card.pack(fill='x', padx=10, pady=10)
        
        tk.Label(personal_card, text="Personal Information", font=('Arial', 14, 'bold'), 
                bg=self.colors['card_bg'], fg=self.colors['primary']).pack(pady=10)
        
        personal_fields = [
            ("Full Name:", "name"),
            ("Email Address:", "email"),
            ("Phone Number:", "phone"),
            ("Location (City, State):", "location"),
            ("LinkedIn Profile:", "linkedin"),
            ("Website/Portfolio:", "website")
        ]
        
        self.entries = {}
        for label, key in personal_fields:
            frame = tk.Frame(personal_card, bg=self.colors['card_bg'])
            frame.pack(fill='x', padx=20, pady=5)
            
            tk.Label(frame, text=label, width=18, anchor='w', 
                    bg=self.colors['card_bg'], font=('Arial', 10)).pack(side='left')
            entry = tk.Entry(frame, width=40, font=('Arial', 10))
            entry.pack(side='left', fill='x', expand=True, padx=5)
            self.entries[key] = entry
        
        # Professional Details Card
        professional_card = tk.Frame(scrollable_frame, bg=self.colors['card_bg'], relief='raised', bd=2)
        professional_card.pack(fill='x', padx=10, pady=10)
        
        tk.Label(professional_card, text="Professional Details", font=('Arial', 14, 'bold'),
                bg=self.colors['card_bg'], fg=self.colors['primary']).pack(pady=10)
        
        # Industry selection
        industry_frame = tk.Frame(professional_card, bg=self.colors['card_bg'])
        industry_frame.pack(fill='x', padx=20, pady=5)
        tk.Label(industry_frame, text="Industry:", width=18, anchor='w', 
                bg=self.colors['card_bg'], font=('Arial', 10)).pack(side='left')
        
        self.industry_var = tk.StringVar(value='technology')
        industries = [('Technology', 'technology'), ('Healthcare', 'healthcare'), 
                     ('Finance', 'finance'), ('Marketing', 'marketing'), ('Education', 'education')]
        
        for text, value in industries:
            rb = tk.Radiobutton(industry_frame, text=text, value=value,
                               variable=self.industry_var, bg=self.colors['card_bg'],
                               command=self.on_industry_change)
            rb.pack(side='left', padx=10)
        
        professional_fields = [
            ("Current Role/Title:", "role"),
            ("Years of Experience:", "years"),
            ("Key Skills (comma separated):", "skills"),
            ("Company/Organization:", "company")
        ]
        
        for label, key in professional_fields:
            frame = tk.Frame(professional_card, bg=self.colors['card_bg'])
            frame.pack(fill='x', padx=20, pady=5)
            
            tk.Label(frame, text=label, width=18, anchor='w', 
                    bg=self.colors['card_bg'], font=('Arial', 10)).pack(side='left')
            entry = tk.Entry(frame, width=40, font=('Arial', 10))
            entry.pack(side='left', fill='x', expand=True, padx=5)
            self.entries[key] = entry
        
        # Industry Facts Display
        self.facts_frame = tk.Frame(scrollable_frame, bg=self.colors['light_bg'])
        self.facts_frame.pack(fill='x', padx=10, pady=10)
        self.update_industry_facts()
        
        # Action Buttons
        button_frame = tk.Frame(scrollable_frame, bg=self.colors['light_bg'])
        button_frame.pack(fill='x', pady=20)
        
        generate_btn = tk.Button(button_frame, text="✨ Generate Professional Resume", 
                               font=('Arial', 12, 'bold'),
                               bg=self.colors['secondary'], fg='white',
                               command=self.generate_resume)
        generate_btn.pack(pady=10)
        
        # Pack scrollable area
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def on_industry_change(self):
        self.update_industry_facts()
    
    def update_industry_facts(self):
        # Clear existing facts
        for widget in self.facts_frame.winfo_children():
            widget.destroy()
        
        industry = self.industry_var.get()
        facts = self.industry_facts[industry]
        
        # Create facts card
        facts_card = tk.Frame(self.facts_frame, bg=self.colors['card_bg'], relief='raised', bd=2)
        facts_card.pack(fill='x', padx=10, pady=10)
        
        tk.Label(facts_card, text=f"Industry Facts - {industry.title()}", 
                font=('Arial', 14, 'bold'), bg=self.colors['card_bg'], fg=self.colors['primary']).pack(pady=10)
        
        # Display industry metrics
        metrics_text = f"• Average Salary: {facts['metrics']['avg_salary']}\n"
        metrics_text += f"• Growth Rate (2024-2025): {facts['metrics']['growth_rate']}\n"
        metrics_text += f"• Job Demand: {facts['metrics']['demand']}"
        
        metrics_label = tk.Label(facts_card, text=metrics_text, justify='left',
                               bg=self.colors['card_bg'], font=('Arial', 10))
        metrics_label.pack(pady=5)
        
        # Suggested skills
        skills_text = "• In-Demand Skills: " + ", ".join(facts['skills'][:5])
        skills_label = tk.Label(facts_card, text=skills_text, justify='left',
                              bg=self.colors['card_bg'], font=('Arial', 10))
        skills_label.pack(pady=5)
        
        # Company examples
        companies = ", ".join(self.real_companies[industry][:3])
        companies_label = tk.Label(facts_card, text=f"• Top Employers: {companies}", justify='left',
                                 bg=self.colors['card_bg'], font=('Arial', 10))
        companies_label.pack(pady=5)
    
    def create_preview_tab(self):
        # Preview header
        header_frame = tk.Frame(self.preview_tab, bg=self.colors['light_bg'])
        header_frame.pack(fill='x', pady=10)
        
        tk.Label(header_frame, text="Professional Resume Preview", 
                font=('Arial', 16, 'bold'), bg=self.colors['light_bg']).pack()
        
        # Action buttons
        btn_frame = tk.Frame(self.preview_tab, bg=self.colors['light_bg'])
        btn_frame.pack(fill='x', pady=10)
        
        tk.Button(btn_frame, text="📄 Download PDF Resume", 
                 font=('Arial', 10, 'bold'),
                 bg=self.colors['secondary'], fg='white',
                 command=self.generate_pdf).pack(side='left', padx=5)
        
        tk.Button(btn_frame, text="🔄 Generate New Version", 
                 font=('Arial', 10),
                 bg=self.colors['accent'], fg='white',
                 command=self.generate_resume).pack(side='left', padx=5)
        
        # Preview text area with scrollbar
        preview_container = tk.Frame(self.preview_tab, bg=self.colors['card_bg'], relief='sunken', bd=2)
        preview_container.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.preview_text = scrolledtext.ScrolledText(preview_container, 
                                                     font=('Courier', 10),
                                                     width=80, height=25,
                                                     bg='white', fg='black')
        self.preview_text.pack(fill='both', expand=True, padx=5, pady=5)
    
    def generate_resume(self):
        # Collect all data
        data = {}
        for key, entry in self.entries.items():
            data[key] = entry.get().strip()
        
        if not data['name']:
            messagebox.showerror("Error", "Please enter your name to generate resume")
            return
        
        # Set default values for empty fields
        industry = self.industry_var.get()
        industry_info = self.industry_facts[industry]
        
        defaults = {
            'role': f'{industry.title()} Professional',
            'years': '3',
            'skills': ', '.join(industry_info['skills'][:5]),
            'company': random.choice(self.real_companies[industry]) if industry in self.real_companies else 'Leading Company'
        }
        
        for key, default in defaults.items():
            if not data[key]:
                data[key] = default
        
        # Generate professional content
        resume_content = self.generate_professional_content(data, industry)
        
        # Display in preview
        self.preview_text.delete('1.0', tk.END)
        self.preview_text.insert('1.0', resume_content)
        
        # Switch to preview tab
        self.notebook.select(1)
        
        messagebox.showinfo("Success", "Professional resume generated! Ready for download.")
    
    def generate_professional_content(self, data, industry):
        # Real industry-specific achievements
        achievements = self.get_industry_achievements(industry, data)
        
        # Build the resume
        resume = f"{'='*70}\n"
        resume += f"{data['name'].upper():^70}\n"
        resume += f"{'='*70}\n\n"
        
        # Contact information
        contact_info = []
        if data['email']: contact_info.append(data['email'])
        if data['phone']: contact_info.append(data['phone'])
        if data['location']: contact_info.append(data['location'])
        if data['linkedin']: contact_info.append(f"LinkedIn: {data['linkedin']}")
        if data['website']: contact_info.append(f"Portfolio: {data['website']}")
        
        resume += " | ".join(contact_info) + "\n\n"
        
        # Professional Summary
        resume += "PROFESSIONAL SUMMARY\n"
        resume += "-" * 50 + "\n"
        summary = self.generate_summary(data, industry)
        resume += f"{summary}\n\n"
        
        # Core Competencies
        resume += "CORE COMPETENCIES\n"
        resume += "-" * 50 + "\n"
        skills_list = [skill.strip() for skill in data['skills'].split(',')]
        resume += " • " + " • ".join(skills_list[:8]) + "\n\n"
        
        # Professional Experience
        resume += "PROFESSIONAL EXPERIENCE\n"
        resume += "-" * 50 + "\n"
        resume += f"{data['role']} | {data['company']}\n"
        resume += f"2022 - Present | {data['location']}\n\n"
        
        for i, achievement in enumerate(achievements[:4], 1):
            resume += f"{i}. {achievement}\n"
        resume += "\n"
        
        # Industry Insights
        resume += "INDUSTRY EXPERTISE\n"
        resume += "-" * 50 + "\n"
        industry_insights = self.get_industry_insights(industry)
        for insight in industry_insights:
            resume += f"• {insight}\n"
        resume += "\n"
        
        # Education (template)
        resume += "EDUCATION\n"
        resume += "-" * 50 + "\n"
        resume += "Bachelor's Degree in Relevant Field | University Name | 2018-2022\n"
        resume += "GPA: 3.6 | Dean's List | Relevant Coursework\n\n"
        
        resume += f"Generated on: {datetime.now().strftime('%B %d, %Y')}"
        
        return resume
    
    def generate_summary(self, data, industry):
        summaries = {
            'technology': [
                f"Technology professional with {data['years']}+ years of experience in software development and system architecture. Proven track record in delivering scalable solutions at {data['company']}.",
                f"Senior {data['role']} specializing in cloud technologies and agile methodologies. Experienced in leading development teams and implementing CI/CD pipelines."
            ],
            'healthcare': [
                f"Dedicated healthcare professional with {data['years']}+ years of experience in patient care and medical administration. Committed to improving healthcare outcomes at {data['company']}.",
                f"Experienced {data['role']} with expertise in healthcare operations and patient service delivery. Skilled in medical terminology and healthcare compliance."
            ],
            'finance': [
                f"Finance professional with {data['years']}+ years of experience in financial analysis and risk management. Demonstrated success in driving profitability at {data['company']}.",
                f"Senior {data['role']} specializing in financial modeling and investment strategies. Proven ability to analyze market trends and deliver data-driven insights."
            ],
            'marketing': [
                f"Marketing professional with {data['years']}+ years of experience in digital marketing and brand strategy. Successfully increased market presence for {data['company']}.",
                f"Creative {data['role']} with expertise in multi-channel marketing campaigns. Proven ability to drive engagement and conversion through data-driven strategies."
            ],
            'education': [
                f"Education professional with {data['years']}+ years of experience in curriculum development and student engagement. Committed to academic excellence at {data['company']}.",
                f"Experienced {data['role']} with expertise in educational technology and instructional design. Skilled in creating inclusive learning environments."
            ]
        }
        return random.choice(summaries[industry])
    
    def get_industry_achievements(self, industry, data):
        achievements = {
            'technology': [
                f"Developed and deployed scalable applications serving 10,000+ daily users at {data['company']}",
                f"Implemented CI/CD pipelines reducing deployment time by 65% and improving team productivity",
                f"Led migration to cloud infrastructure (AWS/Azure) resulting in 40% cost savings annually",
                f"Mentored 3 junior developers and conducted code reviews improving code quality by 30%",
                f"Optimized database queries reducing API response time from 2s to 200ms"
            ],
            'healthcare': [
                f"Managed patient care for 50+ daily appointments while maintaining 95% patient satisfaction scores",
                f"Implemented electronic health records system improving data accuracy by 45% at {data['company']}",
                f"Developed patient education materials increasing treatment adherence by 35%",
                f"Coordinated with cross-functional teams to streamline patient intake process reducing wait times by 25%"
            ],
            'finance': [
                f"Analyzed financial data for ${random.randint(5,20)}M portfolio identifying 15% cost optimization opportunities",
                f"Developed risk assessment models that reduced financial exposure by 30% at {data['company']}",
                f"Prepared quarterly financial reports for executive leadership influencing strategic decisions",
                f"Automated financial reporting processes saving 20 hours per week in manual work"
            ],
            'marketing': [
                f"Executed digital marketing campaigns generating {random.randint(5000,20000)} leads with 15% conversion rate",
                f"Increased social media engagement by 85% through strategic content planning at {data['company']}",
                f"Optimized SEO strategy improving organic traffic by 120% over 6 months",
                f"Managed marketing budget of ${random.randint(50,200)}K achieving 300% ROI on campaigns"
            ],
            'education': [
                f"Developed and implemented curriculum for {random.randint(5,15)} courses with 90% student satisfaction",
                f"Integrated technology tools improving student engagement by 40% at {data['company']}",
                f"Mentored {random.randint(50,200)} students with 95% course completion rate",
                f"Collaborated on accreditation process ensuring 100% compliance with educational standards"
            ]
        }
        return random.sample(achievements[industry], min(4, len(achievements[industry])))
    
    def get_industry_insights(self, industry):
        insights = {
            'technology': [
                "Proficient in latest development frameworks and cloud technologies",
                "Experience with agile methodologies and DevOps practices",
                "Strong problem-solving skills and analytical thinking",
                "Continuous learner staying updated with emerging technologies"
            ],
            'healthcare': [
                "Comprehensive knowledge of healthcare regulations and compliance",
                "Strong patient communication and interpersonal skills",
                "Experience with medical software and EHR systems",
                "Commitment to patient privacy and ethical standards"
            ],
            'finance': [
                "Expertise in financial modeling and data analysis",
                "Strong understanding of regulatory requirements and compliance",
                "Proficient in financial software and Excel advanced functions",
                "Excellent analytical and risk assessment capabilities"
            ],
            'marketing': [
                "Skilled in data-driven marketing strategy and analytics",
                "Experience with digital marketing tools and platforms",
                "Strong creative thinking and content development skills",
                "Proven ability to measure and optimize campaign performance"
            ],
            'education': [
                "Expertise in curriculum development and instructional design",
                "Strong classroom management and student engagement skills",
                "Proficient with educational technology and learning management systems",
                "Commitment to inclusive education and student success"
            ]
        }
        return insights[industry]
    
    def generate_pdf(self):
        content = self.preview_text.get('1.0', tk.END).strip()
        if not content or "Please enter your details" in content:
            messagebox.showerror("Error", "Please generate a resume first")
            return
        
        try:
            # Get name for filename
            name = self.entries['name'].get().strip() or "Professional"
            filename = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF files", "*.pdf")],
                initialfile=f"{name.replace(' ', '_')}_Resume_2025.pdf"
            )
            
            if filename:
                pdf = FPDF()
                pdf.add_page()
                
                # Set font for the PDF
                pdf.set_font("Arial", size=12)
                
                # Split content into lines and add to PDF
                lines = content.split('\n')
                for line in lines:
                    if line.strip():  # Only add non-empty lines
                        # Handle section headers
                        if any(marker in line for marker in ['=====', '-----', 'PROFESSIONAL', 'CORE COMPETENCIES', 
                                                           'EXPERIENCE', 'INDUSTRY', 'EDUCATION']):
                            pdf.set_font("Arial", 'B', 14)
                            pdf.cell(0, 10, line, ln=True)
                            pdf.set_font("Arial", size=12)
                        else:
                            pdf.multi_cell(0, 8, line)
                    pdf.ln(2)
                
                pdf.output(filename)
                messagebox.showinfo("Success", f"PDF resume saved successfully!\n\nLocation: {filename}")
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate PDF: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ProfessionalResumeBuilder(root)
    root.mainloop()