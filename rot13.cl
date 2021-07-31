#!/bin/clisp

(setq alpha "abcdefghijklmnopqrstuvwxyz")

(defun rot13(str)
  (return-from rot13
    (format nil "~{~A~}"
            (loop for i from 0 below (length str) collect
                  (if (find (char str i) alpha :test #'string-equal)
                      (char alpha (mod (+ (position (char str i) alpha :test #'string-equal) 13) 26))
                    (char str i))))))

(format t "~d~%" (rot13 "Hello World!"))
