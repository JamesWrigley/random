;; Problem 12 from Project Euler
;; http://projecteuler.net/problem=12

(defun get-triangle-number (term)
  (if (= term 1)
      1
      (+ term (get-triangle-number (1- term)))))
