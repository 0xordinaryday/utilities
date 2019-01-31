from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfilename
from PyPDF2 import PdfFileMerger, PdfFileReader

root = Tk()
#  ask for the directory at the start
root.directory = filedialog.askdirectory()
root.geometry('350x200')
print(root.directory)

FILE_NAMES = {
    'report': '',
    'plan': '',
    'logs': ''
}


# This is where we launch the file manager bar.
def OpenFile():
    name = askopenfilename(initialdir=root.directory,
                           filetypes=(("PDF File", "*.pdf"),),
                           title="Choose a file."
                           )
    print(name)
    # Using try in case user types in unknown file or closes without choosing a file.
    try:
        with open(name, 'r') as UseFile:
            # print(UseFile.read())
            return name
    except:
        print("No file exists")


def clicked_report():
    filename = OpenFile()
    report_label.configure(text=filename)
    FILE_NAMES['report'] = filename


def clicked_plan():
    filename = OpenFile()
    site_plan_label.configure(text=filename)
    FILE_NAMES['plan'] = filename


def clicked_logs():
    filename = OpenFile()
    logs_label.configure(text=filename)
    FILE_NAMES['logs'] = filename


def merge():
    # filename is a well-formed file path string
    merger = PdfFileMerger()
    merger.append(FILE_NAMES.get('report'))
    merger.append(FILE_NAMES.get('plan'))
    merger.append(FILE_NAMES.get('logs'))
    merger.write("document-output.pdf")


report_label = Label(root, text='Choose report')
report_label.grid(column=0, row=0, sticky=W, padx=5)
report_btn = Button(root, text='Open Report', command=clicked_report)
report_btn.grid(column=0, row=1, sticky=W, padx=5)
site_plan_label = Label(root, text='Choose site plan')
site_plan_label.grid(column=0, row=2, sticky=W, padx=5)
site_plan_btn = Button(root, text='Open site plan', command=clicked_plan)
site_plan_btn.grid(column=0, row=3, sticky=W, padx=5)
logs_label = Label(root, text='Choose logs')
logs_label.grid(column=0, row=4, sticky=W, padx=5)
logs_btn = Button(root, text='Open logs', command=clicked_logs)
logs_btn.grid(column=0, row=5, sticky=W, padx=5)

merge_btn = Button(root, text='Merge PDFs', command=merge, font=('Sans', '10', 'bold'))
merge_btn.grid(column=0, row=6, sticky=W, padx=5, pady=20)

Title = root.title("File Merger")

root.mainloop()
