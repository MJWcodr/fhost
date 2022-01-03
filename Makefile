PREFIX ?= /usr
MANDIR ?= $(PREFIX)/share/man
DOCDIR ?= $(PREFIX)/share/doc/fhost
LIBDIR ?= $(PREFIX)/share/fhost

all:
	@echo Run \'make install\' to install fhost

install:
	@mkdir -p $(PREFIX)/bin
	@mkdir -p $(DESTDIR)$(MANDIR)/man1
	@mkdir -p $(DESTDIR)$(DOCDIR)
	@cp -r src/ $(LIBDIR)
	@cp -r .env $(LIBDIR)
	@cp fhost $(PREFIX)/bin
	@echo 'fhost installed'

uninstall:
	@rm -rf $(LIBDIR)
	@rm -rf $(PREFIX)/bin/fhost
	@echo 'fhost removed'