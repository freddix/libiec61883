Summary:	Streaming library for IEEE1394
Name:		libiec61883
Version:	1.2.0
Release:	14
License:	LGPL
Group:		Libraries
Source0:	http://www.kernel.org/pub/linux/libs/ieee1394/%{name}-%{version}.tar.gz
# Source0-md5:	8af39fff74988073c3ad53fbab147da9
URL:		http://ieee1394.wiki.kernel.org/index.php/Libraries#libiec61883
BuildRequires:	libraw1394-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library is an implementation of IEC 61883, part 1 (CIP, plug
registers, and CMP), part 2 (DV-SD), part 4 (MPEG2-TS), and part 6
(AMDTP). Outside of IIDC, nearly all FireWire multimedia devices use
IEC 61883 protocols.

%package devel
Summary:	libiec61883 header files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libraw1394-devel

%description devel
libiec61883 devel package.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/plug*
%attr(755,root,root) %ghost %{_libdir}/libiec61883.so.0
%attr(755,root,root) %{_libdir}/libiec61883.so.*.*.*
%{_mandir}/man1/plug*.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libiec61883.so
%{_includedir}/libiec61883
%{_pkgconfigdir}/libiec61883.pc

