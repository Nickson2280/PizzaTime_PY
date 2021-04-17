import sys
from PyQt5 import QtGui, QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QFileDialog

days = {1: 'Понедельник', 2: 'Вторник', 3: 'Среда',
        4: 'Четверг', 5: 'Пятница', 6: 'Суббота', 7: 'Воскресенье'}
special_ingredients = ['Сыр Моцарелла', 'Филе куриное', 'Шампиньоны', 'Салями', 'Маслины', 'Бекон', 'Ветчина']


class PizzaTime(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(PizzaTime, self).__init__(parent)
        day = str(days.get(QtCore.QDate.dayOfWeek(QtCore.QDate.currentDate())))
        self.ui = uic.loadUi('Pizza_time_ui.ui')
        self.ui.calender.dateChanged.connect(self.on_date_changed)
        self.ui.calender.setDateTime(QtCore.QDateTime(QtCore.QDate.currentDate()))
        date = self.ui.calender.text()
        self.ui.Ing_comboBox.addItems(special_ingredients)
        self.ui.SelectPizza_btn.clicked.connect(self.order)
        self.ui.AddIng_btn.clicked.connect(self.add_ingredient)
        self.ui.DateAndTime_label.setText('|| Дата: ' + date + ' || День: ' + day + ' ||\n')
        self.ui.setWindowTitle('Время для пиццы')
        self.ui.setWindowIcon(QtGui.QIcon('recipe_pizza_icon.ico'))
        self.ui.show()

    def order(self):
        file_name = QFileDialog.getSaveFileName(self, 'Save file')
        file = open(file_name[0], 'w')
        data = self.ui.DateAndTime_label.text() + '||\n'
        data += '|| ' + self.ui.DescriptionPizza_label.text() + '\n||\n'
        data += '|| Цена: ' + self.ui.Price_label.text() + ' ||\n||'
        file.write(data)
        file.close()
        sys.exit()

    def add_ingredient(self):
        self.ui.DescriptionPizza_label.setText(self.ui.DescriptionPizza_label.text() + '\nДополнительный '
                                                                                       'ингридиент: ' +
                                               self.ui.Ing_comboBox.currentText())

    def on_date_changed(self, q_date):
        dayofweek = str(days.get(QtCore.QDate.dayOfWeek(q_date)))
        if dayofweek == 'Понедельник':
            self.ui.DescriptionPizza_label.setText('Пицца "Маргарита"\n'
                                                   'Состав: соус, сыр Моцарелла ди Буфало, базилик, оливковое масло.')
            pixmap = QtGui.QPixmap('margarita.jpg')
            self.ui.PhotoPizza_label.setPixmap(pixmap)
            self.ui.Price_label.setText('250 UAH')
        if dayofweek == 'Вторник':
            self.ui.DescriptionPizza_label.setText('Пицца "Сицилийская"\n'
                                                   'Состав: анчоусы, итальянский сыр пекорино, томаты.')
            pixmap = QtGui.QPixmap('sicilian.jpg')
            self.ui.PhotoPizza_label.setPixmap(pixmap)
            self.ui.Price_label.setText('260 UAH')
        if dayofweek == 'Среда':
            self.ui.DescriptionPizza_label.setText('Пицца "Дьябло"\n'
                                                   'Состав: колбаски, сыры Моцарелла и Пармезан, грибы шампиньоны и '
                                                   'перец чили.')
            pixmap = QtGui.QPixmap('diablo.jpg')
            self.ui.PhotoPizza_label.setPixmap(pixmap)
            self.ui.Price_label.setText('300 UAH')
        if dayofweek == 'Четверг':
            self.ui.DescriptionPizza_label.setText('Пицца "Гавайская"\n'
                                                   'Состав: ветчина, ананас, лук, зеленый перец или халапеньо, сыр,'
                                                   ' томатный соус.')
            pixmap = QtGui.QPixmap('hawaiian.jpg')
            self.ui.PhotoPizza_label.setPixmap(pixmap)
            self.ui.Price_label.setText('260 UAH')
        if dayofweek == 'Пятница':
            self.ui.DescriptionPizza_label.setText('Пицца "Капричоза"\n'
                                                   'Состав: маринованные помидоры, оливки, сыр Рикотта и Пармезана, '
                                                   'ветчина, оливковое масло, зелень.')
            pixmap = QtGui.QPixmap('capricious.jpg')
            self.ui.PhotoPizza_label.setPixmap(pixmap)
            self.ui.Price_label.setText('300 UAH')
        if dayofweek == 'Суббота':
            self.ui.DescriptionPizza_label.setText('Пицца "Кальцоне"\n'
                                                   'Состав: орегано, грибы, рикотта, ветчина, моцарелла, пармезан.')
            pixmap = QtGui.QPixmap('calzone.jpg')
            self.ui.PhotoPizza_label.setPixmap(pixmap)
            self.ui.Price_label.setText('250 UAH')
        if dayofweek == 'Воскресенье':
            self.ui.DescriptionPizza_label.setText('Пицца "По-неаполитански"\n'
                                                   'Состава: сыр, маслины, колбаса, свежие помидоры, оливковое масло.')
            pixmap = QtGui.QPixmap('napless.jpg')
            self.ui.PhotoPizza_label.setPixmap(pixmap)
            self.ui.Price_label.setText('250 UAH')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = PizzaTime()
    sys.exit(app.exec())
# PhotoPizza_label, DateAndTime_label, DescriptionPizza_label, Price_label
# AddIng_btn, SelectPizza_btn
# Ing_comboBox
# EnableAddIng_checkbox
