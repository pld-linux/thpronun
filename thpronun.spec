Summary:	Thai word pronunciation program
Summary(pl.UTF-8):	Program do wymowy słów tajskich
Name:		thpronun
Version:	0.2.0
Release:	2
License:	GPL v3
Group:		Applications/Text
Source0:	https://linux.thai.net/pub/thailinux/software/thpronun/%{name}-%{version}.tar.xz
# Source0-md5:	35ebb2ff6d687a2fe88bddbb9d8afbd0
URL:		https://linux.thai.net/
BuildRequires:	help2man
BuildRequires:	libdatrie-devel >= 0.2
# C++14
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	libthai-devel
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
thpronun is a program for analyzing pronunciation of Thai words.
The output can be in Thai pronunciation, Romanization, or in any other
phonetic systems. It is designed to be extensible.

%description -l pl.UTF-8
thpronun to program do analizy wymowy słów tajskich. Wyjściem może być
w postaci wymowy tajskiej, romanizacji lub dowolnym innym systemie
fonetycznym. Program jest zaprojektowany jako rozszerzalny.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/gen-lookup-dict
%attr(755,root,root) %{_bindir}/thpronun
%{_datadir}/thpronun
%{_mandir}/man1/thpronun.1*
