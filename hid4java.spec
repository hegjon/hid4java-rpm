#Not released yet
%global revision b010ceedec1c773eb748c23f9ae9729831ad91a8
%global short_sha b010cee

Name: hid4java
Version: 0.4.0
Release: 0.1.git%{short_sha}%{?dist}
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
* Fri Aug 07 2015 Jonny Heggheim <hegjon@gmail.com> - 0.4.0-0.1.gitb010cee
- Inital packaging
