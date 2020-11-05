#encoding:utf-8
from flask import Blueprint,render_template,views,request
import splitList

dlt = Blueprint('dlt',__name__)

@dlt.route('/dlt')
def do_dlt_list():
    fout = open('dlt.txt', encoding='UTF-8')
    lines = fout.readlines()
    lines.sort(reverse=True)
    for line in lines:
        print(line)
    return render_template('dltShowList.html',**locals())

class ChoiceDLTList(views.MethodView):
    def post(self):
        redStr = str(request.form.get('front'))
        blueStr = str(request.form.get('after'))
        operatorType = str(request.form.get('operatorType'))
        no = str(request.form.get('no'))
        print(no)
        print(redStr)
        print(blueStr)
        if operatorType == '0':
            return splitList.runDlt(redStr,blueStr,no)
        elif operatorType == '1':
            return splitList.returnList(redStr,blueStr)
        else:
            return ''
dlt.add_url_rule('/choicelDlt',view_func=ChoiceDLTList.as_view('choiceDLTList'))