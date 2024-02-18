from flask import Flask, render_template, url_for, request, flash, redirect
from flask_mail import Mail, Message
import math
import os
import sqlite3

app = Flask(__name__)
app.secret_key = '12345'
DATABASE = '/tmp/flsite.db'
debug = True
SECRET_KEY = '12345'
app.config.from_object(__name__)

# Настройки для отправки почты
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Укажите сервер почты
app.config['MAIL_PORT'] = 465  # Порт сервера почты
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'rudolfrozenberg04@gmail.com'  # Ваш email
app.config['MAIL_PASSWORD'] = 'jfpc uylw qwxs wkwh '  # Пароль от вашего email  
mail = Mail(app)


# ROUTE #


# ГЛАВНАЯ
@app.route('/')
def main():    
    return render_template('rest/index.html')



# ОБРАТНАЯ СВЯЗЬ
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        msg = Message(subject='Feedback', sender=email, recipients=['rudolfrozenberg04@gmail.com'])
        msg.body = f"From: {name}\nEmail: {email}\nMessage: {message}"
        mail.send(msg)
        return render_template('rest/index.html')
    return render_template('rest/resmail.html')



# УМНОЖЕНИЕ
@app.route('/multiply', methods=['POST', 'GET'])
def multiply():
    try:
        if request.method == 'POST' or 'GET':
           if 'rate' in request.form:
               rate = str(request.form['rate'])
               amount = str(request.form['amount'])
               if ',' in rate and ',' in  amount:
                   rate = float(rate.replace(',', '.'))
                   amount = float(amount.replace(',', '.'))
                   result = rate * amount
                   return render_template('rest/result.html', result=result)
               else:
                   rate = int(request.form['rate'])
                   amount = int(request.form['amount'])
                   result = rate * amount
                   return render_template('rest/result.html', result=result)
        else:
            return "Missing 'rate' parameter in the request."
        return render_template('processes/multiply.html')
    except ValueError:
        flash('Ошибка! Пожалуйста, введите верное значение в поле ввода!')
        return redirect(url_for('processes/multiply'))



# ДЕЛЕНИЕ  
@app.route('/divide', methods=['POST', 'GET'])
def divide():
    try:
        if request.method == 'POST' or 'GET':
           if 'rate' in request.form:
               rate = str(request.form['rate'])
               amount = str(request.form['amount'])
               if ',' in rate and ',' in  amount:
                   rate = float(rate.replace(',', '.'))
                   amount = float(amount.replace(',', '.'))
                   result = rate / amount
                   return render_template('rest/result.html', result=result)
               else:
                   rate = int(request.form['rate'])
                   amount = int(request.form['amount'])
                   result = rate / amount
                   return render_template('rest/result.html', result=result)
        else:
            return "Missing 'rate' parameter in the request."
        return render_template('processes/divide.html')
    except ValueError:
        flash('Ошибка! Пожалуйста, введите верное значение в поле ввода!')
        return redirect(url_for('processes/divide'))
    except ZeroDivisionError:
        flash('Ошибка! На ноль делить нельзя!')
        return redirect(url_for('divide'))



#СЛОЖЕНИЕ
@app.route('/fold', methods=['POST', 'GET'])
def fold():
    try:
        if request.method == 'POST' or 'GET':
           if 'rate' in request.form:
               rate = str(request.form['rate'])
               amount = str(request.form['amount'])
               if ',' in rate and ',' in  amount:
                   rate = float(rate.replace(',', '.'))
                   amount = float(amount.replace(',', '.'))
                   result = rate / amount
                   return render_template('rest/result.html', result=result)
               else:
                   rate = int(request.form['rate'])
                   amount = int(request.form['amount'])
                   result = rate + amount
                   return render_template('rest/result.html', result=result)
        else:
            return "Missing 'rate' parameter in the request."
        return render_template('processes/fold.html')
    except ValueError:
        flash('Ошибка! Пожалуйста, введите верное значение в поле ввода!')
        return redirect(url_for('fold'))



#ВЫЧИТАНИЕ
@app.route('/subtract', methods=['POST', 'GET'])
def subtract():
    try:
        if request.method == 'POST' or 'GET':
           if 'rate' in request.form:
               rate = str(request.form['rate'])
               amount = str(request.form['amount'])
               if ',' in rate and ',' in  amount:
                   rate = float(rate.replace(',', '.'))
                   amount = float(amount.replace(',', '.'))
                   result = rate / amount
                   return render_template('rest/result.html', result=result)
               else:
                   rate = int(request.form['rate'])
                   amount = int(request.form['amount'])
                   result = rate - amount
                   return render_template('rest/result.html', result=result)
        else:
            return "Missing 'rate' parameter in the request."
        return render_template('processes/subtract.html')
    except ValueError:
        flash('Ошибка! Пожалуйста, введите верное значение в поле ввода!')
        return redirect(url_for('subtract'))



# ПОЛИТИКА
@app.route('/rules')
def rules():
    return render_template('rest/rules.html')



# ERRORSHANDLER
@app.errorhandler(404)
def handle_not_found404(e):
    return render_template('errors/error404.html'), 404

@app.errorhandler(500)
def handle_not_found500(e):
    return render_template('errors/error/500.html'), 500

@app.route('/test-error-500')
def test_error():
    raise Exception("Это тестовая ошибка 500")
# ERRORSHANDLER


# ROUTE #

if __name__ == '__main__':
    app.run(debug=True)