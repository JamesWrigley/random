#ifndef HASHER_H
#define HASHER_H

#include <QLabel>
#include <QWidget>
#include <QComboBox>
#include <QLineEdit>
#include <QStringList>
#include <QVBoxLayout>
#include <QHBoxLayout>

class Hasher : public QWidget
{
  Q_OBJECT

 public:
  Hasher(QWidget *parent = 0);

 private:
  void center_window();
  void create_layouts();
  void create_widgets();

  QVBoxLayout *main_vbox;
  QHBoxLayout *title_hbox;
  QHBoxLayout *middle_hbox;
  QHBoxLayout *bottom_hbox;

  QStringList algos;
  QStringList object_types;
  QLabel *main_title;
  QLabel *object_types_label;
  QComboBox *object_types_comboBox;
  QComboBox *algos_comboBox;
  QLineEdit *lineEdit_input;

};

#endif // HASHER_H
