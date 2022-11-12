Name:		texlive-gfscomplutum
Version:	19469
Release:	1
Summary:	A Greek font with a long history
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/greek/gfs/gfscomplutum
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gfscomplutum.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gfscomplutum.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
GFS Complutum derives, via a long development, from a
minuscule-only font cut in the 16th century. An unsatisfactory
set of majuscules were added in the early 20th century, but its
author died before he could complete the revival of the font.
The Greek Font Society has released this version, which has a
new set of majuscules.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/gfscomplutum/GFSComplutum-Regular.afm
%{_texmfdistdir}/fonts/enc/dvips/gfscomplutum/gpcomplutum.enc
%{_texmfdistdir}/fonts/map/dvips/gfscomplutum/gfscomplutum.map
%{_texmfdistdir}/fonts/opentype/public/gfscomplutum/GFSPolyglot.otf
%{_texmfdistdir}/fonts/tfm/public/gfscomplutum/gcomplutum8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfscomplutum/gcomplutum8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfscomplutum/gcomplutumo8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfscomplutum/gcomplutumo8r.tfm
%{_texmfdistdir}/fonts/type1/public/gfscomplutum/GFSComplutum-Regular.pfb
%{_texmfdistdir}/fonts/vf/public/gfscomplutum/gcomplutum8a.vf
%{_texmfdistdir}/fonts/vf/public/gfscomplutum/gcomplutumo8a.vf
%{_texmfdistdir}/tex/latex/gfscomplutum/gfscomplutum.sty
%{_texmfdistdir}/tex/latex/gfscomplutum/lgrcomplutum.fd
%doc %{_texmfdistdir}/doc/fonts/gfscomplutum/OFL-FAQ.txt
%doc %{_texmfdistdir}/doc/fonts/gfscomplutum/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/gfscomplutum/README
%doc %{_texmfdistdir}/doc/fonts/gfscomplutum/README.TEXLIVE
%doc %{_texmfdistdir}/doc/fonts/gfscomplutum/gfscomplutum.pdf
%doc %{_texmfdistdir}/doc/fonts/gfscomplutum/gfscomplutum.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
