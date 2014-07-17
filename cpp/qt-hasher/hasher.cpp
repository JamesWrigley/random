#include <QDir>
#include <QApplication>
#include <QDesktopWidget>
#include "hasher.h"

Hasher::Hasher(QWidget *parent) : QWidget(parent)
{
  create_layouts();
  create_widgets();

  // Set up connections
  QObject::connect(object_types_comboBox, SIGNAL(currentIndexChanged(int)),
                   this, SLOT(change_object_type(int)));
  QObject::connect(open_file_button, SIGNAL(clicked(bool)),
                   this, SLOT(select_file()));

  // Packing
  title_hbox->addStretch();
  title_hbox->addWidget(main_title);
  title_hbox->addStretch();

  middle_hbox->addWidget(object_types_label);
  middle_hbox->addWidget(object_types_comboBox);
  middle_hbox->addWidget(lineEdit_input);

  bottom_hbox->addStretch();
  bottom_hbox->addWidget(algos_comboBox);
  bottom_hbox->addWidget(open_file_button);
  bottom_hbox->addWidget(hash_button);

  main_vbox->addStretch();
  main_vbox->addLayout(title_hbox);
  main_vbox->addStretch();
  main_vbox->addLayout(middle_hbox);
  main_vbox->addLayout(bottom_hbox);

  this->setLayout(main_vbox);
  this->setWindowTitle("Qt Hasher");
  this->setFixedSize(375, 220);
  this->center_window();
}


void Hasher::create_layouts()
{
  main_vbox = new QVBoxLayout(this);
  title_hbox = new QHBoxLayout();
  middle_hbox = new QHBoxLayout();
  bottom_hbox = new QHBoxLayout();
}


void Hasher::create_widgets()
{
  algos << "MD5" << "SHA-1" << "SHA-224" << "SHA-256" << "SHA-384" << "SHA-512";
  object_types << "String/Text" << "File";

  main_title = new QLabel("Qt Hasher", this);
  main_title->setFont(QFont("Inconsolata", 40));
  object_types_label = new QLabel("Object type:", this);

  open_file_button = new QPushButton("Open File", this);
  open_file_button->setDisabled(true);
  hash_button = new QPushButton("Hash", this);

  object_types_comboBox = new QComboBox(this);
  object_types_comboBox->addItems(object_types);
  algos_comboBox = new QComboBox(this);
  algos_comboBox->addItems(algos);
  algos_comboBox->setCurrentIndex(1);

  lineEdit_input = new QLineEdit(this);
}


void Hasher::select_file()
{
  lineEdit_input->setText(QFileDialog::getOpenFileName(this, "Select File", QDir::homePath()));
}


void Hasher::change_object_type(int index)
{
  if (index == 0)
    {
      open_file_button->setDisabled(true);
      lineEdit_input->setReadOnly(false);
      lineEdit_input->setText("");
    }
  else if (index == 1)
    {
      open_file_button->setDisabled(false);
      lineEdit_input->setText("");
      lineEdit_input->setReadOnly(true);
    }
}


void Hasher::center_window()
{
  QRect screen_geo = QApplication::desktop()->screenGeometry();
  QWidget *main_window = QWidget::window();

  int x = (screen_geo.width() - 375) / 2;
  int y = (screen_geo.height() - 220) / 2;

  main_window->move(x,y);
}
