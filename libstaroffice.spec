#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libstaroffice
Version  : 0.0.6
Release  : 2
URL      : https://dev-www.libreoffice.org/src/libstaroffice-0.0.6.tar.xz
Source0  : https://dev-www.libreoffice.org/src/libstaroffice-0.0.6.tar.xz
Summary  : A library for reading StarOffice documents
Group    : Development/Tools
License  : LGPL-2.1 MPL-2.0-no-copyleft-exception
Requires: libstaroffice-bin
Requires: libstaroffice-lib
Requires: libstaroffice-license
BuildRequires : doxygen
BuildRequires : pkgconfig(librevenge-0.0)
BuildRequires : pkgconfig(librevenge-generators-0.0)
BuildRequires : pkgconfig(zlib)

%description
The purpose of libstaroffice is to build a filter for old StarOffice's
documents(.sdc, .sdw, ...) based on librevenge(see
https://sourceforge.net/p/libwpd/wiki/librevenge/ and
http://www.documentliberation.org/projects/ ).

%package bin
Summary: bin components for the libstaroffice package.
Group: Binaries
Requires: libstaroffice-license

%description bin
bin components for the libstaroffice package.


%package dev
Summary: dev components for the libstaroffice package.
Group: Development
Requires: libstaroffice-lib
Requires: libstaroffice-bin
Provides: libstaroffice-devel

%description dev
dev components for the libstaroffice package.


%package doc
Summary: doc components for the libstaroffice package.
Group: Documentation

%description doc
doc components for the libstaroffice package.


%package lib
Summary: lib components for the libstaroffice package.
Group: Libraries
Requires: libstaroffice-license

%description lib
lib components for the libstaroffice package.


%package license
Summary: license components for the libstaroffice package.
Group: Default

%description license
license components for the libstaroffice package.


%prep
%setup -q -n libstaroffice-0.0.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534635699
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1534635699
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/libstaroffice
cp COPYING.LGPL %{buildroot}/usr/share/doc/libstaroffice/COPYING.LGPL
cp COPYING.MPL %{buildroot}/usr/share/doc/libstaroffice/COPYING.MPL
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sd2raw
/usr/bin/sd2svg
/usr/bin/sd2text
/usr/bin/sdc2csv
/usr/bin/sdw2html

%files dev
%defattr(-,root,root,-)
/usr/include/libstaroffice-0.0/libstaroffice/STOFFDocument.hxx
/usr/include/libstaroffice-0.0/libstaroffice/libstaroffice.hxx
/usr/lib64/libstaroffice-0.0.so
/usr/lib64/pkgconfig/libstaroffice-0.0.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libstaroffice/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libstaroffice-0.0.so.0
/usr/lib64/libstaroffice-0.0.so.0.0.6

%files license
%defattr(-,root,root,-)
/usr/share/doc/libstaroffice/COPYING.LGPL
/usr/share/doc/libstaroffice/COPYING.MPL
