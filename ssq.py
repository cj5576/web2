#encoding:utf-8
from flask import Blueprint,views,request,render_template
import splitList

ssq = Blueprint('ssq',__name__)

@ssq.route('/ssq')
def do_ssq_list():
    fout = open('ssq.txt', encoding='UTF-8')
    lines = fout.readlines()
    lines.sort(reverse=True)
    for line in lines:
        print(line)
    # randSum = random.randint(1,9)
    return render_template('ssqShowList.html',**locals())



class ChoiceSSQList(views.MethodView):
    def post(self):
        redStr = str(request.form.get('red'))
        blueStr = str(request.form.get('blue'))
        operatorType = str( request.form.get( 'operatorType' ) )
        no = str(request.form.get('no'))
        print(no)
        print(redStr)
        print(blueStr)
        if operatorType == '0':
            return splitList.runSsq(redStr,blueStr,no)
        elif operatorType == '1':
            return splitList.returnList2(redStr,blueStr)
        else:
            return ''

ssq.add_url_rule('/choicelSsq',view_func=ChoiceSSQList.as_view('choiceSSQList'))