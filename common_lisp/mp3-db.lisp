(defvar *db* nil)

(defun track-info (title artist year)
  (list :title title :artist artist :year year))

(defun add-track (track)
  (push track *db*))

(defun print-db (db)
  (dolist (cd db)
    (format t "~{~a:~10t~a~%~}~%" cd)))
