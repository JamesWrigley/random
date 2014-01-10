#include <gtkmm/application.h>
#include "helloworld.h"

int main(int argc, char *argv[])
{
    Glib::RefPtr<Gtk::Application> app = Gtk::Application::create(argc, 
                                                                  argv,
                                                                  "org.gtkmm.examples.base");
    HelloWorld window;

    return app->run(window);

}
