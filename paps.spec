%define	version	0.6.6
%define release	%mkrel 2

Summary:	Text to Postscript Converter Using Pango
Name:		paps
Version:	%{version}
Release:	%{release}
License:	LGPL
Group:		Publishing
URL:		http://paps.sourceforge.net/
Source0:	http://paps.sourceforge.net/%{name}-%{version}.tar.bz2
Patch0:		paps-0.6.1-destdir.patch.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	pango-devel
BuildRequires:  doxygen

%description
%{name} reads a UTF-8 encoded file and generates a PostScript
language rendering of the file. The rendering is done by creating
outline curves through the pango ft2 backend.

%package -n	%{_lib}paps-static-devel
Summary:	Development related files for %{name}
Group:		Development/Other

%description -n	%{_lib}paps-static-devel
%{name} reads a UTF-8 encoded file and generates a PostScript
language rendering of the file. The rendering is done by creating
outline curves through the pango ft2 backend.

%prep
%setup -q
%patch0 -p1 -b .destdir
autoreconf --force --install

%build
%configure2_5x
make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -rf ./html
mv %{buildroot}%{_datadir}/doc/libpaps/html ./
rmdir -p %{buildroot}%{_datadir}/doc/libpaps || true
# doxygen generated something funny
rm -f html/docs__*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README
%{_bindir}/*
%{_mandir}/man1/%{name}.*.bz2


%files -n %{_lib}paps-static-devel
%defattr(-,root,root)
%doc ChangeLog html
%{_includedir}/*
%{_libdir}/*.a
