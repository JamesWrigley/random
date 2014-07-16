#include "hasher.h"
#include <QApplication>

int main(int argc, char *argv[])
{
  QApplication app(argc, argv);
  Hasher mainwindow;
  mainwindow.show();

  return app.exec();
}
