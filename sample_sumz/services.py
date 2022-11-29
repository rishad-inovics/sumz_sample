from sample_sumz.models import Questions
import xlrd

def reading_questions(excel_file):
    workbook = xlrd.open_workbook(file_contents=excel_file.read())
    for sheet_name in workbook.sheet_names():
        details = []
        sheet = workbook.sheet_by_name(sheet_name)
        for rowno in range(sheet.nrows):
            details.append(sheet.row(rowno))
        for detail in details:
            question = detail[0].value
            option1 = detail[1].value
            option2 = detail[2].value
            option3 = detail[3].value
            option4 = detail[4].value
            correct_option = detail[5].value
            questions = Questions.objects.create(text=question, option1=option1, option2=option2,
                                                 option3=option3, option4=option4,
                                                 correct_option=correct_option, sheet=sheet_name,
                                                 file_name=excel_file)
    return questions
