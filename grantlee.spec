%define		qtver		4.6.2

Summary:	grantlee
Summary(pl.UTF-8):	grantlee
Name:		grantlee
Version:	0.1.0
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	http://downloads.grantlee.org/%{name}-v%{version}.tar.gz
# Source0-md5:	3ec14214f30cc86d10c3cab2d062ff3e
URL:		http://www.gitorious.org/grantlee/pages/Home
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtScript-devel >= %{qtver}
BuildRequires:	QtSql-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	QtWebKit-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.84
BuildRequires:	cmake >= 2.8.0
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Grantlee is a string template engine based on the Django template
system and written in Qt.

#%description -l pl.UTF-8

%package devel
Summary:	Header files for grantlee
Summary(pl.UTF-8):	Pliki nagłówkowe dla grantlee
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for grantlee.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla grantlee.

%prep
%setup -q -n %{name}-v%{version}

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/ldconfig
%postun	-p	/sbin/ldconfig

%files
%defattr(644,root,root,755)
%dir %{_libdir}/grantlee
%dir %{_libdir}/grantlee/0.1
%attr(755,root,root) %{_libdir}/grantlee/0.1/grantlee_defaultfilters.so
%attr(755,root,root) %{_libdir}/grantlee/0.1/grantlee_defaulttags.so
%attr(755,root,root) %{_libdir}/grantlee/0.1/grantlee_loadertags.so
%attr(755,root,root) %{_libdir}/grantlee/0.1/grantlee_scriptabletags.so
%attr(755,root,root) %ghost %{_libdir}/libgrantlee_core.so.?
%attr(755,root,root) %{_libdir}/libgrantlee_core.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgrantlee_gui.so.?
%attr(755,root,root) %{_libdir}/libgrantlee_gui.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgrantlee_core.so
%attr(755,root,root) %{_libdir}/libgrantlee_gui.so
%{_includedir}/grantlee_core.h
%{_includedir}/%{name}
%{_libdir}/grantlee/0.1/GrantleeUse.cmake
%{_libdir}/grantlee/GrantleeConfig.cmake
%{_libdir}/grantlee/GrantleeConfigVersion.cmake
