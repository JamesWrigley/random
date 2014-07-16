#include <QDesktopWidget>
#include <QApplication>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QLabel>
#include <QFont>
#include "hasher.h"

Hasher::Hasher(QWidget *parent) : QWidget(parent)
{
  // Create the layouts
  QVBoxLayout *main_vbox = new QVBoxLayout(this);
  QHBoxLayout *title_hbox = new QHBoxLayout();

  QLabel *title = new QLabel("Qt Hasher", this);
  title->setFont(QFont("Inconsolata", 40));

  // Packing
  title_hbox->addStretch();
  title_hbox->addWidget(title);
  title_hbox->addStretch();

  main_vbox->addLayout(title_hbox);
  main_vbox->addStretch();

  this->setLayout(main_vbox);
  this->setWindowTitle("Qt Hasher");
  this->setFixedSize(350, 200);
  this->center();
}

void Hasher::center()
{
  QRect screen_geo = QApplication::desktop()->screenGeometry();
  QWidget *main_window = QWidget::window();

  int x = (screen_geo.width() - 350) / 2;
  int y = (screen_geo.height() - 200) / 2;

  main_window->move(x,y);
}
