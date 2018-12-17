;;; gerrit-download-autoloads.el --- automatically extracted autoloads
;;
;;; Code:

(add-to-list 'load-path (directory-file-name
                         (or (file-name-directory #$) (car load-path))))


;;;### (autoloads nil "gerrit-download" "gerrit-download.el" (0 0
;;;;;;  0 0))
;;; Generated autoloads from gerrit-download.el

(autoload 'gerrit-download-gnus-from-email "gerrit-download" "\
Parse an email from jenkins in Gnus and get the project and change-id.

\(fn)" t nil)

(autoload 'gerrit-download "gerrit-download" "\


\(fn PROJECT REVIEW-ID)" t nil)

(if (fboundp 'register-definition-prefixes) (register-definition-prefixes "gerrit-download" '("gerrit-")))

;;;***

;; Local Variables:
;; version-control: never
;; no-byte-compile: t
;; no-update-autoloads: t
;; coding: utf-8
;; End:
;;; gerrit-download-autoloads.el ends here
