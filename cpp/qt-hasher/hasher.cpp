#include <QtGui>
#include "hasher.h"

Hasher::Hasher(QWidget *parent) : QWidget(parent)
{
  QStringList algos;
  algos << "MD5" << "SHA-1" << "SHA-224" << "SHA-256" << "SHA-384" << "SHA-512";

  QStringList object_types;
  object_types << "String/Text" << "File";

  // Create the layouts
  QVBoxLayout *main_vbox = new QVBoxLayout(this);
  QHBoxLayout *title_hbox = new QHBoxLayout();
  QHBoxLayout *middle_hbox = new QHBoxLayout();
  QHBoxLayout *bottom_hbox = new QHBoxLayout();

  // Create widgets
  QLabel *title = new QLabel("Qt Hasher", this);
  title->setFont(QFont("Inconsolata", 40));

  QLabel *object_type_label = new QLabel("Object type:", this);

  QComboBox *object_types_comboBox = new QComboBox(this);
  object_types_comboBox->addItems(object_types);

  QComboBox *algos_comboBox = new QComboBox(this);
  algos_comboBox->addItems(algos);
  algos_comboBox->setCurrentIndex(1);

  QLineEdit *lineEdit_input = new QLineEdit(this);

  // Packing
  title_hbox->addStretch();
  title_hbox->addWidget(title);
  title_hbox->addStretch();

  middle_hbox->addWidget(object_type_label);
  middle_hbox->addWidget(algos_comboBox);
  middle_hbox->addWidget(lineEdit_input);

  bottom_hbox->addStretch();
  bottom_hbox->addWidget(object_types_comboBox);

  main_vbox->addLayout(title_hbox);
  main_vbox->addStretch();
  main_vbox->addLayout(middle_hbox);
  main_vbox->addLayout(bottom_hbox);

  this->setLayout(main_vbox);
  this->setWindowTitle("Qt Hasher");
  this->setFixedSize(375, 220);
  this->center();
}

void Hasher::center()
{
  QRect screen_geo = QApplication::desktop()->screenGeometry();
  QWidget *main_window = QWidget::window();

  int x = (screen_geo.width() - 375) / 2;
  int y = (screen_geo.height() - 220) / 2;

  main_window->move(x,y);
}
