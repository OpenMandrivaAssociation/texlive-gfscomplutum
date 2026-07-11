%global tl_name gfscomplutum
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	A Greek font with a long history
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/greek/gfs/gfscomplutum
License:	ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gfscomplutum.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gfscomplutum.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
GFS Complutum derives, via a long development, from a minuscule-only
font cut in the 16th century. An unsatisfactory set of majuscules were
added in the early 20th century, but its author died before he could
complete the revival of the font. The Greek Font Society has released
this version, which has a new set of majuscules.

