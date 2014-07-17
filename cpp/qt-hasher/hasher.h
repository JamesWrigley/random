#ifndef HASHER_H
#define HASHER_H

#include <QLabel>
#include <QWidget>
#include <QComboBox>
#include <QLineEdit>
#include <QStringList>
#include <QPushButton>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QFileDialog>

class Hasher : public QWidget
{
  Q_OBJECT

 public:
  Hasher(QWidget *parent = 0);

  private slots:
    void change_object_type(int);
    void select_file();

 private:
    void center_window();
    void create_layouts();
    void create_widgets();

    QStringList algos;
    QStringList object_types;

    QVBoxLayout *main_vbox;
    QHBoxLayout *title_hbox;
    QHBoxLayout *middle_hbox;
    QHBoxLayout *bottom_hbox;

    QLabel *main_title;
    QLabel *object_types_label;
    QComboBox *object_types_comboBox;
    QComboBox *algos_comboBox;
    QLineEdit *lineEdit_input;
    QPushButton *open_file_button;
    QPushButton *hash_button;
};

#endif // HASHER_H
