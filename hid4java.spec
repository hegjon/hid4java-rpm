#Not released yet
%define revision 1e9ef8066326a858e6158b5131ef8e5d6af64d53
%define short_revision 1e9ef80

Name: hid4java
Version: 0.4.0
Release: 0.1.git%{short_revision}%{?dist}
Summary: Java wrapper for the hidapi library

License: MIT
URL: http://github.com/gary-rowe/hid4java
Source0: https://github.com/gary-rowe/%{name}/archive/%{revision}.tar.gz
Patch0: load-system-hidapi-usb-library.patch
BuildArch: noarch

BuildRequires: maven-local
BuildRequires: mvn(net.java.dev.jna:jna)

Requires: libhidapi-libusb.so.0

%description
hid4java supports USB HID devices through a common API. The API is very simple
but provides great flexibility such as support for feature reports and blocking
reads with timeouts. Attach/detach events are provided to allow applications to
respond instantly to device availability.


%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n hid4java-%{revision}

%patch0 -p1

find -name '*.so' -print -delete
find -name '*.dylib' -print -delete
find -name '*.dll' -print -delete

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc AUTHORS README.md
%license LICENSE

%files javadoc -f .mfiles-javadoc
%doc AUTHORS README.md
%license LICENSE

%changelog
* Aug 07 2015 Jonny Heggheim <hegjon@gmail.com> - 0.4.0-0.1.git1e9ef80
- Inital packaging
