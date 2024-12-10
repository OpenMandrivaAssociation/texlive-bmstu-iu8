Name:		texlive-bmstu-iu8
Version:	72693
Release:	1
Summary:	A class for IU8 reports
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bmstu-iu8
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bmstu-iu8.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bmstu-iu8.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package consists of a class file and style files for
writing reports at the IU8 department of IU faculty of BMSTU
(Bauman Moscow State Technical University). The class defines
all headings, structure elements and other things in respect of
Russian standard GOST 7.32-2017. But there are correctives to
be compatible with our local IU8 department requirements.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/bmstu-iu8
%doc %{_texmfdistdir}/doc/latex/bmstu-iu8

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
