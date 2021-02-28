Summary:	Open-source implementation of Secure Real-time Transport Protocol
Summary(pl.UTF-8):	Otwarta implementacja protokołu Secure Real-time Transport Protocol
Name:		libsrtp2
Version:	2.3.0
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/cisco/libsrtp/releases
Source0:	https://github.com/cisco/libsrtp/archive/v%{version}/libsrtp-%{version}.tar.gz
# Source0-md5:	da38ee5d9c31be212a12964c22d7f795
URL:		https://github.com/cisco/libsrtp
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	libpcap-devel
BuildRequires:	openssl-devel >= 1.0.1
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
Obsoletes:	srtp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libSRTP library is an open-source implementation of Secure
Real-time Transport Protocol (SRTP).

%description -l pl.UTF-8
Biblioteka libSRTP to otwarta implementacja protokołu SRTP (Secure
Real-time Transport Protocol).

%package devel
Summary:	Header files for SRTP library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki SRTP
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libpcap-devel
Requires:	openssl-devel >= 1.0.1
Requires:	zlib-devel
Obsoletes:	srtp-devel

%description devel
Header files for SRTP library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki SRTP.

%package static
Summary:	Static SRTP library
Summary(pl.UTF-8):	Statyczna biblioteka SRTP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	srtp-static

%description static
Static SRTP library.

%description static -l pl.UTF-8
Statyczna biblioteka SRTP.

%package apidocs
Summary:	API documentation for SRTP library
Summary(pl.UTF-8):	Dokumentacja API biblioteki SRTP
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for SRTP library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki SRTP.

%prep
%setup -q -n libsrtp-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure \
	--enable-openssl

%{__make} shared_library
%{__make} all
%{__make} libsrtp2doc

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README.md
%attr(755,root,root) %{_libdir}/libsrtp2.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsrtp2.so
%{_pkgconfigdir}/libsrtp2.pc
%{_includedir}/srtp2

%files static
%defattr(644,root,root,755)
%{_libdir}/libsrtp2.a

%files apidocs
%defattr(644,root,root,755)
%doc doc/html/*
