#ifndef HASHER_H
#define HASHER_H

#include <QWidget>

class Hasher : public QWidget
{
  Q_OBJECT

 public:
  Hasher(QWidget *parent = 0);

 private:
  void center();
};

#endif // HASHER_H
