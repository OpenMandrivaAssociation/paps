%define	version	0.6.8
%define release	%mkrel 1
%define staticdevelname %mklibname -s -d paps

Summary:	Text to Postscript Converter Using Pango
Name:		paps
Version:	%{version}
Release:	%{release}
License:	LGPL
Group:		Publishing
URL:		http://paps.sourceforge.net/
Source0:	http://paps.sourceforge.net/%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	pango-devel
BuildRequires:  doxygen

%description
%{name} reads a UTF-8 encoded file and generates a PostScript
language rendering of the file. The rendering is done by creating
outline curves through the pango ft2 backend.

%package -n	%{staticdevelname}
Summary:	Development related files for %{name}
Group:		Development/Other

%description -n	%{staticdevelname}
%{name} reads a UTF-8 encoded file and generates a PostScript
language rendering of the file. The rendering is done by creating
outline curves through the pango ft2 backend.

%prep
%setup -q
#autoreconf --force --install

%build
%configure2_5x
make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README doxygen-doc/html/*
%{_bindir}/*
%{_mandir}/man1/%{name}.*.bz2


%files -n %{staticdevelname}
%defattr(-,root,root)
%doc ChangeLog
%{_includedir}/*
%{_libdir}/*.a
