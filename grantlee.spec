%define		qt_ver		4.7.1

Summary:	Grantlee - set of frameworks for use with Qt
Summary(pl.UTF-8):	Grantlee - zbiór szkieletów do wykorzystania z Qt
Name:		grantlee
Version:	0.3.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.grantlee.org/%{name}-%{version}.tar.gz
# Source0-md5:	195763a3238f51f8885881fc8012cd83
Patch0:		%{name}-link.patch
URL:		http://www.gitorious.org/grantlee/pages/Home
BuildRequires:	QtCore-devel >= %{qt_ver}
BuildRequires:	QtGui-devel >= %{qt_ver}
BuildRequires:	QtScript-devel >= %{qt_ver}
BuildRequires:	QtSql-devel >= %{qt_ver}
BuildRequires:	QtTest-devel >= %{qt_ver}
BuildRequires:	QtWebKit-devel >= %{qt_ver}
BuildRequires:	cmake >= 2.8.0
BuildRequires:	qt4-build >= %{qt_ver}
BuildRequires:	qt4-qmake >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Grantlee is a string template engine based on the Django template
system and written using Qt.

%description -l pl.UTF-8
Grantlee to silnik szablonów oparty na systemie szablonów Django i
napisany przy użyciu Qt.

%package devel
Summary:	Header files for grantlee libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek grantlee
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtCore-devel >= %{qt_ver}
# only _gui (textdocument) library
Requires:	QtGui-devel >= %{qt_ver}

%description devel
Header files for grantlee libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek grantlee.

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG GOALS README
%attr(755,root,root) %{_libdir}/libgrantlee_core.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgrantlee_core.so.0
%attr(755,root,root) %{_libdir}/libgrantlee_gui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgrantlee_gui.so.0
%dir %{_libdir}/grantlee
%dir %{_libdir}/grantlee/0.3
%attr(755,root,root) %{_libdir}/grantlee/0.3/grantlee_defaultfilters.so
%attr(755,root,root) %{_libdir}/grantlee/0.3/grantlee_defaulttags.so
%attr(755,root,root) %{_libdir}/grantlee/0.3/grantlee_i18ntags.so
%attr(755,root,root) %{_libdir}/grantlee/0.3/grantlee_loadertags.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgrantlee_core.so
%attr(755,root,root) %{_libdir}/libgrantlee_gui.so
%{_includedir}/grantlee_core.h
%{_includedir}/grantlee_templates.h
%{_includedir}/grantlee
%{_libdir}/cmake/grantlee
