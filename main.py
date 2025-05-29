import customtkinter as ctk
from tkinter import filedialog, messagebox
import PyPDF2
import os
import threading

class PDFMergerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("PDF Merger Pro 🔗")
        self.geometry("620x550")
        self.iconbitmap("app.ico")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.pdf_files = []

        self.current_theme = "dark"

        title = ctk.CTkLabel(self, text="🔗 PDF Merger", font=("Arial", 24, "bold"))
        title.pack(pady=15)

        self.select_button = ctk.CTkButton(self, text="📂 Selecionar PDFs", command=self.select_files, width=200)
        self.select_button.pack(pady=10)

        self.listbox = ctk.CTkTextbox(self, height=220, width=500, font=("Arial", 14))
        self.listbox.configure(state="disabled")
        self.listbox.pack(pady=10)

        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=10)

        self.btn_up = ctk.CTkButton(button_frame, text="⬆ Subir", width=120, command=self.move_up)
        self.btn_up.grid(row=0, column=0, padx=5)

        self.btn_down = ctk.CTkButton(button_frame, text="⬇ Descer", width=120, command=self.move_down)
        self.btn_down.grid(row=0, column=1, padx=5)

        self.btn_remove = ctk.CTkButton(button_frame, text="🗑 Remover", width=120, command=self.remove_file)
        self.btn_remove.grid(row=0, column=2, padx=5)

        self.save_button = ctk.CTkButton(self, text="💾 Salvar PDF Final", fg_color="green", hover_color="darkgreen", command=self.thread_save_pdf)
        self.save_button.pack(pady=20)

        self.theme_button = ctk.CTkButton(self, text="🌓 Alternar Tema", command=self.toggle_theme, width=140)
        self.theme_button.pack()

        self.status_label = ctk.CTkLabel(self, text="", font=("Arial", 14))
        self.status_label.pack()

    def toggle_theme(self):
        if self.current_theme == "dark":
            ctk.set_appearance_mode("light")
            self.current_theme = "light"
        else:
            ctk.set_appearance_mode("dark")
            self.current_theme = "dark"

    def select_files(self):
        files = filedialog.askopenfilenames(title="Selecionar arquivos PDF", filetypes=[("PDF", "*.pdf")])
        if files:
            for file in files:
                if file not in self.pdf_files:
                    self.pdf_files.append(file)
            self.refresh_listbox()

    def refresh_listbox(self):
        self.listbox.configure(state="normal")
        self.listbox.delete("1.0", "end")
        for i, f in enumerate(self.pdf_files):
            self.listbox.insert("end", f"{i+1}. {os.path.basename(f)}\n")
        self.listbox.configure(state="disabled")

    def move_up(self):
        current = self.get_selected_index()
        if current > 0:
            self.pdf_files[current], self.pdf_files[current - 1] = self.pdf_files[current - 1], self.pdf_files[current]
            self.refresh_listbox()

    def move_down(self):
        current = self.get_selected_index()
        if current < len(self.pdf_files) - 1:
            self.pdf_files[current], self.pdf_files[current + 1] = self.pdf_files[current + 1], self.pdf_files[current]
            self.refresh_listbox()

    def remove_file(self):
        current = self.get_selected_index()
        if current is not None:
            del self.pdf_files[current]
            self.refresh_listbox()

    def get_selected_index(self):
        try:
            line = self.listbox.index("insert").split(".")[0]
            return int(line) - 1
        except:
            return 0

    def thread_save_pdf(self):
        threading.Thread(target=self.save_pdf).start()

    def save_pdf(self):
        if not self.pdf_files:
            messagebox.showwarning("Aviso", "Nenhum arquivo PDF selecionado!")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF", "*.pdf")], title="Salvar PDF mesclado como")
        if not save_path:
            return

        self.status_label.configure(text="🔄 Mesclando arquivos PDF, aguarde...")
        try:
            merger = PyPDF2.PdfMerger()
            for pdf in self.pdf_files:
                merger.append(pdf)
            merger.write(save_path)
            merger.close()
            self.status_label.configure(text="✅ PDF mesclado salvo com sucesso!")
        except Exception as e:
            self.status_label.configure(text="")
            messagebox.showerror("Erro", f"Erro ao mesclar PDF:\n{e}")

if __name__ == "__main__":
    app = PDFMergerApp()
    app.mainloop()
