Name: hid4java
Version: 0.3.1
Release: 1%{?dist}
Summary: Java wrapper for the hidapi library

Group: System Environment/Libraries
License: MIT
URL: http://github.com/gary-rowe/hid4java
Source0: https://github.com/gary-rowe/%{name}/archive/%{version}.tar.gz
Patch0: load-system-hidapi-usb-library.patch
BuildArch: noarch

BuildRequires: maven-local
BuildRequires: mvn(net.java.dev.jna:jna)

Requires: java-headless >= 1:1.6.0
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
%setup -q

%patch0 -p1

find -name '*.so' -print -delete
find -name '*.dylib' -print -delete
find -name '*.dll' -print -delete

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc AUTHORS README.md
%license LICENSE

%files javadoc -f .mfiles-javadoc
%doc AUTHORS README.md
%license LICENSE

%changelog
* Wed Jun 10 2015 Jonny Heggheim <hegjon@gmail.com> - 0.3.1-1
- Inital packaging
