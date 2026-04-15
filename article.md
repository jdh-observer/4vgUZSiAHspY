---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.19.1
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

<!-- #region editable=true slideshow={"slide_type": ""} tags=["title"] -->
# Exploring the Archived Web through AI Assisted Document Discovery
<!-- #endregion -->

<!-- #region slideshow={"slide_type": ""} tags=["contributor"] -->
### Victor Harbo  Johnston [![orcid](https://orcid.org/sites/default/files/images/orcid_16x16.png)](https://orcid.org/0000-0003-0087-1220) 
Aarhus University
<!-- #endregion -->

<!-- #region slideshow={"slide_type": ""} tags=["contributor"] -->
### Brian  Balsun-Stanton [![orcid](https://orcid.org/sites/default/files/images/orcid_16x16.png)](https://orcid.org/0000-0003-4932-7912) 
Macquarie University
<!-- #endregion -->

<!-- #region jp-MarkdownHeadingCollapsed=true slideshow={"slide_type": ""} tags=["contributor"] -->
### Helle Strandgaard  Jensen [![orcid](https://orcid.org/sites/default/files/images/orcid_16x16.png)](https://orcid.org/0000-0002-8623-9586) 
Aarhus University
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["contributor"] -->
### Christian Kaalund  Kjelsen [![orcid](https://orcid.org/sites/default/files/images/orcid_16x16.png)](https://orcid.org/ORCID_ID_IF_EXIST) 
Aarhus University
<!-- #endregion -->

<!-- #region slideshow={"slide_type": ""} tags=["contributor"] -->
### Jørn  Thøgersen [![orcid](https://orcid.org/sites/default/files/images/orcid_16x16.png)](https://orcid.org/0009-0000-8837-1057) 
Aarhus University

<!-- #endregion -->

<!-- #region tags=["copyright"] -->
[![cc-by](https://licensebuttons.net/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/) 
©<AUTHOR or ORGANIZATION / FUNDER>. Published by De Gruyter in cooperation with the University of Luxembourg Centre for Contemporary and Digital History. This is an Open Access article distributed under the terms of the [Creative Commons Attribution License CC-BY](https://creativecommons.org/licenses/by/4.0/)

<!-- #endregion -->

<!-- #region slideshow={"slide_type": ""} tags=["keywords"] -->
Archived Web, Large Language Model, Document Discovery, Methodology
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["abstract"] -->
Archival collections of born digital sources often consist of millions, even billions of items. Discovering relevant sources for traditional close reading in this type of collection is a challenge because text-based queries return unreadable amounts of possibly relevant material. This means that systems historians traditionally have used for finding relevant sources are challenged.

Besides the difficulty of finding relevant sources for close reading, a particular kind of digital archive: web archives, presents even further challenges to historians. Unlike many other digital collections, web archives do not collect, curate, and make their material available in ways that are modelled on already existing archival practices. This means that besides the difficulties of finding sources for close reading, these archives also challenge the fundamental structures that enable the application of source criticism creating a double bind in terms of working with archived web material in ways that resemble the way historians traditionally work.

With this article we propose a method that leads researchers to find the sources most relevant for their research question in an extremely vast and messy corpus with unclear and mixed provenance. Our method lets historians and other researchers work from a problem-oriented approach where the research questions lead the search for relevant source material. This method is inspired by the way historians generally work with discovery in archival collections. 

The proposed method utilises a large language model (LLM) to categorise documents from a web archive collection with an uncertain provenance based on categories constructed from our initial research question. In doing so, the paper contributes to the field of digital history with a methodological approach for discovering source material in a collection with a large degree of uncertain provenance. This particular focus sets the article apart from many approaches in the field of digital history, which focus not on document discovery but aggregated analysis of source material. 

<!-- #endregion -->

<!-- #region slideshow={"slide_type": ""} -->
## Introduction
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"8dxoz": [{"id": "13014974/U4NRYK6X", "source": "zotero"}], "v5m1j": [{"id": "13014974/U4NRYK6X", "source": "zotero"}]}} slideshow={"slide_type": ""} -->
Knowing the origins, the provenance, of a source is key in source criticism. Hence, imagine being a historian who works with an archive where you know almost nothing about the origins of the sources: nothing about why the archive collected them, who created them in the first place, how they relate to other sources in the archive, not even the date they were created. 

This is not a thought experiment, unfortunately, rather these are only some of the “manyfold barriers” of working with the archived web as a primary source (<cite id="v5m1j"><a href="#zotero%7C13014974%2FU4NRYK6X">(Bell et al., 2022)</a></cite>).
Archived web material is, in short, fragmented copies of the past web stored in web archives (<cite id="56gu2"><a href="#zotero%7C13014974%2FYRJU2TH6">(Brügger, 2018)</a></cite>). One can choose to look only at a single webpage, like BBC.co.uk, and contextualise it within an institution, the British Broadcasting Corporation. And archives with clearly demarcated, structured collections with rich metadata like the UK Government Web Archive, also make the information needed to apply the principles of source criticism available to some degree (<cite id="8dxoz"><a href="#zotero%7C13014974%2FU4NRYK6X">(Bell et al., 2022)</a></cite>). However, using websites from only one institution does not reflect the interactive nature and use of the web, and, for the most part, the web is not made up of sites with easily distinguishable authors and institutional contexts. Furthermore, historians will, in most cases, not know which websites of interest to their enquiry have existed, as no central register or search engine covers the past web. The largest and oldest web archive in the world, The Internet Archive, only supports search by URL, not the text on the actual pages in the archive, let alone search for different filetypes.

In this article we discuss how using the archived web as a source challenges the tradition(s) of source discovery and criticism because of the way the web has been archived and made available. Based on these discussions, we explore the extent to which it is possible to use a large language model to set up a workflow for detailed document discovery attuned to the ways historians have traditionally worked with discovery of sources.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
## Historians ignore the archived web as a source
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"0gz8b": [{"id": "13014974/T8A4A2LN", "source": "zotero"}], "1q44k": [{"id": "13014974/Z86YG7B9", "source": "zotero"}], "3z6y9": [{"id": "13014974/4DH2IGN8", "source": "zotero"}], "56gu2": [{"id": "13014974/YRJU2TH6", "source": "zotero"}], "97gw9": [{"id": "", "source": "zotero"}], "a9o69": [{"id": "13014974/MEFA9S5G", "source": "zotero"}], "h2jl9": [{"id": "13014974/VMGM7V76", "source": "zotero"}], "ig0zy": [{"id": "13014974/MEFA9S5G", "source": "zotero"}], "ixnae": [{"id": "13014974/YRJU2TH6", "source": "zotero"}], "t1u64": [{"id": "13014974/WMS9YB9E", "source": "zotero"}], "xzydr": [{"id": "13014974/9RUGHY4C", "source": "zotero"}], "yldee": [{"id": "13014974/MEFA9S5G", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
Archived web material represents one of the richest but most overlooked collections of sources for contemporary historians, however many scholars do not know of their potential or even their existence (<cite id="3z6y9"><a href="#zotero%7C13014974%2F4DH2IGN8">(Winters, 2018)</a></cite>,<cite id="xzydr"><a href="#zotero%7C13014974%2F9RUGHY4C">(Winters, 2017)</a></cite>). To forego use of the archived web is to overlook valuable primary sources, as these corpora are rich with information from the last three decades. Much of the material from the archived web is authored by people who would otherwise never have made it into the historical record (<cite id="ig0zy"><a href="#zotero%7C13014974%2FMEFA9S5G">(Milligan, 2019)</a></cite>). In the words of Ian Milligan: “One cannot write most histories of the 1990s or later without reference to web archives, or at the very least to do so would be to neglect a major medium of the period.” (<cite id="a9o69"><a href="#zotero%7C13014974%2FMEFA9S5G">(Milligan, 2019)</a></cite>, 3). This circumstance will only become more central with the ongoing shift from analogue to digital processes in modern society (<cite id="t1u64"><a href="#zotero%7C13014974%2FWMS9YB9E">(Brügger, 2016)</a></cite>). 

The Internet Archive started archiving the web in 1996. They began storing websites for preservation and future use. Their collection is not the only available web archive collection, but by far the oldest and most expansive (<cite id="0gz8b"><a href="#zotero%7C13014974%2FT8A4A2LN">(Rackley, 2010)</a></cite>). There are multiple ways to archive websites and the way it is done has many implications for how the material can be used—a situation that is parallel to how collection and preservation practices impact the use of all other archives. The most comprehensive and widespread way of archiving is through web crawling. In web crawling, a list of desired websites (a seed list) is fed to an archiving software that systematically retrieves the webpages on the list one by one. At each website, the crawler follows all the hyperlinks linking to other websites, these are also saved. The crawler continues this iterative process as far 'away' from the originally designated websites as it was instructed to (<cite id="97gw9"><a href="#zotero%7C13014974%2FA3AHKIRC">(Brown, 2006)</a></cite>). Because of this archiving methodology, it is not possible to predict in advance what websites are archived or what content they contain. It is possible to manually check the content of the seed list, but with lists of more than a handful of websites, it is not feasible to check all the hyperlinks linking to other websites. For this reason, it is not possible to predict the resulting items in or size of a web crawl. This means that the provenance of the items in the archive is uncertain; we simply do not know what the archive contains and where its content is derived from.

The most common way of interacting with archived websites from the Internet Archive is through their Wayback Machine, which is a URL-based playback engine. The Wayback Machine can be a good entry point if you already know which URLs you are interested in. If you don’t have this knowledge, then the archive can be difficult to explore (<cite id="7edqh"><a href="#zotero%7C13014974%2F4PZKJWL9">(Hartelius, 2020)</a></cite>). When historians are interpreting their questions and working with the archived web it can feel like looking for a needle in a haystack, without being able to grasp the size of the haystack.

Previous literature has shown that it is primarily scholars with a background in media and information studies rather than historians who have used the archived web as a historical source (<cite id="1q44k"><a href="#zotero%7C13014974%2FZ86YG7B9">(Milligan, 2015)</a></cite>, <cite id="h2jl9"><a href="#zotero%7C13014974%2FVMGM7V76">(Schafer &#38; Thierry, 2018)</a></cite>, <cite id="yldee"><a href="#zotero%7C13014974%2FMEFA9S5G">(Milligan, 2019)</a></cite>). This has resulted in a historiography with a strong focus on the web as a medium. Often it is the web itself, entire top-level domains, or a group of websites which have been central in these investigations (<cite id="22rwb"><a href="#zotero%7C13014974%2FM27V95EN">(Brügger &#38; Milligan, 2019)</a></cite>). This is what Niels Brügger has called history *of* the web: using websites to study the history of websites (<cite id="56gu2"><a href="#zotero%7C13014974%2FYRJU2TH6">(Brügger, 2018)</a></cite>). Another way of using the archived web as a source is to conduct history *with* the web: using websites to study the history of broader societal or cultural changes and continuities, or, in other words, using archived web material to do what we might think of as more traditional historical research. This difference in use also entails that historians’ interest in knowledge of provenance differs from how it has been described for the archived web previously (<cite id="ixnae"><a href="#zotero%7C13014974%2FYRJU2TH6">(Brügger, 2018)</a></cite>). In the existing descriptions of a website’s provenance, it has been knowledge of the archived version of the website which was the focus (e.g. the time of the crawl). To write a history with the web as a source, it is rather the provenance of its original creation from when it was live online that is pivotal, as this will enable the historian to analyse why it was created, by whom, with what intent, etc. The historian’s understanding of provenance therefore foregrounds the context of the webpage that was once live (even if knowing the provenance of the archived version is, of course, also important).

The possible lack of methodological integrity that can come from working with historical sources using digital methods from other fields is only one pitfall which has been discussed by digital historians (<cite id="aqz4r"><a href="#zotero%7C13014974%2FA3AE6CWL">(Hiltmann, 2022)</a></cite>). Others include lack of transparency and reproducibility when using certain digital tools, as well as the fact that especially text mining tools does not consider change over time (<cite id="7uamw"><a href="#zotero%7C13014974%2FU4YE7LCF">(Guldi, 2023)</a></cite>, <cite id="jbc18"><a href="#zotero%7C13014974%2FD8JRBXDW">(Schwandt, 2022)</a></cite>). In the document discovery method, we have aimed to create transparency in the use of the LLM by documenting the processes for data collection, pre-processing, prompting and specific LLM processing, by using the possibilities for transparency provided by the Journal of Digital History.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
## The role of discovery in source criticism and problem-driven approaches
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"2kquo": [{"id": "13014974/YPXEER39", "source": "zotero"}], "3hmw5": [{"id": "13014974/SXLWFB6V", "source": "zotero"}], "8qwro": [{"id": "13014974/M5LZ38BE", "source": "zotero"}], "w0jh7": [{"id": "13014974/E4JPU32E", "source": "zotero"}], "x8jvr": [{"id": "13014974/MXG3KLIA", "source": "zotero"}], "xb8v8": [{"id": "13014974/SXLWFB6V", "source": "zotero"}], "xrmtk": [{"id": "13014974/BD33C2S7", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
For the past to become history, a set of sources must be interpreted and be presented as part of an argument (<cite id="2kquo"><a href="#zotero%7C13014974%2FYPXEER39">(<i>Digital History &#38; Argument White Paper – Roy Rosenzweig Center for History and New Media</i>, n.d.)</a></cite>). Historical enquiry begins with a question or a wonder, and the resulting research is closely tied to the research question that the historian has asked (<cite id="3hmw5"><a href="#zotero%7C13014974%2FSXLWFB6V">(Schrag, 2021)</a></cite>). The questions are then tackled through a search for sources and an investigation of the often-complex material to conduct a historical analysis of the topic under investigation (<cite id="x8jvr"><a href="#zotero%7C13014974%2FMXG3KLIA">(Iggers, 1997)</a></cite>). Searching for sources, analysing them and placing one's study within the existing historiography is part of a dialectic process which informs and hones the questions the historian asks (<cite id="xb8v8"><a href="#zotero%7C13014974%2FSXLWFB6V">(Schrag, 2021)</a></cite>). Today framing of research questions can also be helped by digital tools (<cite id="w0jh7"><a href="#zotero%7C13014974%2FE4JPU32E">(Gibbs &#38; Owens, 2013)</a></cite>). No matter how historians are asking, framing, or exploring their questions, a problem-driven approach has long been the norm, meaning that the search for sources is driven by the questions asked.

Archival discovery plays a central role in the problem driven approach, as it is central to the source criticism that is at the center when answering a research question. By providing crucial context about a source’s provenance, the systems in place for collection and curation of sources help to judge the context in which the source was made (<cite id="8qwro"><a href="#zotero%7C13014974%2FM5LZ38BE">(Putnam, 2016)</a></cite>, <cite id="xrmtk"><a href="#zotero%7C13014974%2FBD33C2S7">(Jensen, 2021)</a></cite>). This context helps us understand who created the source and why. As mentioned above, knowing the context of archived web material is extremely difficult. This is a great contrast to consulting a physical or digitised archive. Here historians often know what to expect from the archive. For instance, one would expect to find newspapers in a newspaper archive, government papers in a government archive, and correspondence by letters in a personal archive from the 18th century. Usually, one would also know which newspapers were included in the newspaper archive, what government office to find papers from in which part of the collection from a certain government and which person that was central in the personal archive. This is not the case with web archives. They can have all kinds of textual expressions (in the broadest sense) from anyone (with the technical skills, hardware, and access needed).

Archived web material is, like all historical archives, an incomplete record, with not all sites, nor all elements on a given site, being preserved. The central challenge in working with archived web material is nonetheless that there is too much of it. It is not feasible to read individual pages manually even for a relatively small corpus, meaning that some form of distant or targeted reading is required. One promising strategy to find relevant sources in the age of abundance is to conduct LLM-assisted document discovery.

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
## Digital document discovery as part of digital history
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"1x3f9": [{"id": "13014974/UBWELQHJ", "source": "zotero"}], "4lvn8": [{"id": "13014974/M2BM4YLQ", "source": "zotero"}], "7cmfe": [{"id": "13014974/XPKGWRJ3", "source": "zotero"}], "7uamw": [{"id": "13014974/U4YE7LCF", "source": "zotero"}], "aqz4r": [{"id": "13014974/A3AE6CWL", "source": "zotero"}], "jbc18": [{"id": "13014974/D8JRBXDW", "source": "zotero"}], "m5xj1": [{"id": "13014974/4T525T4G", "source": "zotero"}], "wkbyb": [{"id": "13014974/ARKRT8VZ", "source": "zotero"}], "x6zb7": [{"id": "13014974/BNPP5TCN", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
The most common method in history is still close reading of text (<cite id="m5xj1"><a href="#zotero%7C13014974%2F4T525T4G">(Ohrvik, 2024)</a></cite>). However, the number of available sources has skyrocketed with the emergence of the World Wide Web in the 1990’s and 2000’s, digitisation of source material and a multitude of born-digital sources and the ways in which historians consult their sources have changed (<cite id="x6zb7"><a href="#zotero%7C13014974%2FBNPP5TCN">(Milligan, 2022)</a></cite>, <cite id="4lvn8"><a href="#zotero%7C13014974%2FM2BM4YLQ">(Blouin &#38; Rosenberg, 2011)</a></cite>).

When historians work with digital sources from a quantitative, distant reading perspective, they usually know what their sources consists of. They know whether they are censuses, newspapers, petitions, etc. They also know the record producer (government, petitioners e.g.). Newspapers might be a more exceptional case as they have many different contributors, which is why users have complained about the ‘noise’ in newspaper archives (<cite id="fg5ul"><a href="#zotero%7C13014974%2F4WPBFKJ3">(Jarlbrink &#38; Snickars, 2017)</a></cite>). As mentioned above, this homogeneity is not the case with the archived web. Here, we face an unprecedented amount of material with very little knowledge of the provenance of the sources we interpret.

The complexity of using archived web material as a source thus to some extend defies recent calls in digital history to put the sources and historical domain expertise first, because we do not know the data (<cite id="aqz4r"><a href="#zotero%7C13014974%2FA3AE6CWL">(Hiltmann, 2022)</a></cite>, <cite id="wkbyb"><a href="#zotero%7C13014974%2FARKRT8VZ">(Crowston &#38; Lemercier, 2019)</a></cite>, <cite id="7cmfe"><a href="#zotero%7C13014974%2FXPKGWRJ3">(Jensen et al., 2024)</a></cite>). However, what we propose below is a method for finding relevant sources in a vast and messy pile of material. The methodology has been applied to a smaller test corpus of 9,267 sources and afterwards to a corpus consisting of all archived material from the domain kidlink.org. 

The Kidlink domain started as an idea with a rather controlled and limited scope as part of a weeklong festival celebrating children’s culture (<cite id="ym5a9"><a href="#zotero%7C13014974%2FM8SBUIIL">(“Datakontakt Med Heila Verda,” 1992)</a></cite>). Originally, the founder Odd de Presno wanted his daughter to chat with a granddaughter of an American friend using a big screen to display the two girls live chat on the Internet. But the word about the idea of transatlantic communication for children spread, and in the 14 days leading up to the festival, more than 260 children from Norway, the United States and Canada had used the network.  After the festival, the project continued running, now under the name Kidlink. During the next year, more than 26,000 kids from 31 countries participated in the Internet-based communication exchange (<cite id="x7nsb"><a href="#zotero%7C13014974%2FTPFH3GFB">(Mizell &#38; Others, 1992)</a></cite>).

This corpus of Kidlink material consists of 384,700 sources in total, of which 293,679 are textual records. With this approach, we develop a digital method for document discovery that reflects how historians work. We preserve the complexity and the messy nature of the historical sources that were the past web that produced a great variety and complexity in provenance.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
## Large language models in archives
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"0wtoj": [{"id": "13014974/2F7XDPYF", "source": "zotero"}], "2ljcf": [{"id": "13014974/R6DMZBGE", "source": "zotero"}], "32i0h": [{"id": "13014974/VG77SSLT", "source": "zotero"}], "3rmrp": [{"id": "13014974/5MS8Y9E4", "source": "zotero"}], "42sbr": [{"id": "13014974/F7B6QW9F", "source": "zotero"}], "4egpc": [{"id": "13014974/R6DMZBGE", "source": "zotero"}], "ckoy9": [{"id": "13014974/HZ8VZRCQ", "source": "zotero"}], "fi71m": [{"id": "", "source": "zotero"}], "fxfoa": [{"id": "13014974/FXKB3AE7", "source": "zotero"}], "gk0yy": [{"id": "13014974/QG4UX8UE", "source": "zotero"}], "kh31u": [{"id": "13014974/U4NRYK6X", "source": "zotero"}], "ldgup": [{"id": "13014974/DQHCMEA2", "source": "zotero"}], "s3l68": [{"id": "13014974/M5LZ38BE", "source": "zotero"}], "to33u": [{"id": "13014974/QG4UX8UE", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
Historians have pointed out a number of problems with keyword searching in vast digital collections (<cite id="42sbr"><a href="#zotero%7C13014974%2FF7B6QW9F">(Hitchcock, 2013)</a></cite>, <cite id="s3l68"><a href="#zotero%7C13014974%2FM5LZ38BE">(Putnam, 2016)</a></cite>). The concerns have been raised for multiple types of material, ranging from digitised newspaper collections with bad OCR quality to web archive collections with millions of documents returning an abundance of results (<cite id="ckoy9"><a href="#zotero%7C13014974%2FHZ8VZRCQ">(Torget, 2023)</a></cite>,<cite id="gk0yy"><a href="#zotero%7C13014974%2FQG4UX8UE">(Winters &#38; Prescott, 2019)</a></cite>). The issue of discoverability of sources in born-digital cultural heritage collections is also discussed in the field of archival studies. This field has seen the use of LLMs for metadata enhancement and curatorial work with large collections, most of these are still on an exploratory level (<cite id="4egpc"><a href="#zotero%7C13014974%2FR6DMZBGE">(Canning &#38; Jaillant, 2025)</a></cite>, <cite id="3rmrp"><a href="#zotero%7C13014974%2F5MS8Y9E4">(Baron, 2025)</a></cite>, <cite id="0wtoj"><a href="#zotero%7C13014974%2F2F7XDPYF">(Reusens et al., 2025)</a></cite>). Canning and Jaillant argue that heritage institutions need to apply automated curatorial practices when they take material into their collections as part of the appraisal of material (<cite id="2ljcf"><a href="#zotero%7C13014974%2FR6DMZBGE">(Canning &#38; Jaillant, 2025)</a></cite>). The practice of appraising born-digital material before it becomes part of a collection contrasts how web archive collections have been collected up until now. Most often, no such curation has been applied to web archive collections. These collections are big and messy and require new ways of searching (<cite id="to33u"><a href="#zotero%7C13014974%2FQG4UX8UE">(Winters &#38; Prescott, 2019)</a></cite>). We believe that a methodological approach as the one presented in this article can be used as a new way of finding relevant sources in web archives for a specific research question.

Previous solutions for working with archived web data from an analytical perspective have mostly focused on the work which takes place when a corpus has already been identified (<cite id="ldgup"><a href="#zotero%7C13014974%2FDQHCMEA2">(Ruest et al., 2022)</a></cite>, <cite id="fxfoa"><a href="#zotero%7C13014974%2FFXKB3AE7">(Sherratt et al., n.d.)</a></cite>). We, however, want to identify relevant sources within a vast web archive collection. Drawing on user-centred perspectives from archival studies, it can be argued that the traditional approach for historians is not the approach that earlier developed methods and approaches have been developed for (<cite id="32i0h"><a href="#zotero%7C13014974%2FVG77SSLT">(Nix et al., 2025)</a></cite>). One of the only other instances of work that starts from the historian’s perspective has tried to identify what researchers need in terms of search and discovery when working with such archives (<cite id="fi71m"><a href="#zotero%7C13014974%2FU4NRYK6X">(Bell et al., 2022)</a></cite>). They describe the difficulty of curating a set of websites in relation to a theme, because it might only be subsections of very large sites that are of interest. What they suggest is to: “seed an automated approach, by compiling a list of keywords, by selecting a few exemplar websites, or perhaps by using the Wikipedia entry for an event of interest. The web sphere idea could mitigate against the complexity identified in the extraction of hierarchies by curating pages around a concept, which could be a government function without explicitly defining its position in a hierarchy.” (<cite id="kh31u"><a href="#zotero%7C13014974%2FU4NRYK6X">(Bell et al., 2022)</a></cite>).

What we see in this quote is the centring of a problem-driven approach that can be linked to a broad semantic field which would be present in a wide range of documents across web-spheres, sites, pages, and elements. This thematic framing recognises that issues are rarely defined by a single phrase, named entity, or easily defined text snippet. Seeing that the article was written in 2022, there was not the same widespread employment or possibilities of LLMs as today. These models can make search queries based on the called-for combination of ‘Wikipediaish’ knowledge, examples from websites and keywords. Making use of an LLM as a discovery tool thus seems like a logical extension of Bell et al.’s argument. However, as we suggest below, the plain historical knowledge of a Wikipedia entry can be replaced with the detailed knowledge of a domain expert. 

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
# Document discovery
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
As introduced above, the archived web has seldom been used as a source for historical research. This section presents and explores our methodological approach which can be seen as an alternative to traditional search in vast collections. The following section presents how the method has been developed and on what material it has been tested. The methodology consists of multiple parts such as finding test material and creating categories based on domain specific questions for the document discovery framework.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["hermeneutics"] -->
## Corpus
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"6vzpx": [{"id": "", "source": "zotero"}], "6w4po": [{"id": "", "source": "zotero"}], "7edqh": [{"id": "", "source": "zotero"}], "84pxm": [{"id": "", "source": "zotero"}], "art3o": [{"id": "", "source": "zotero"}], "fo2lr": [{"id": "", "source": "zotero"}], "gsghp": [{"id": "", "source": "zotero"}], "i7rhf": [{"id": "", "source": "zotero"}], "jgq2b": [{"id": "", "source": "zotero"}], "k3526": [{"id": "", "source": "zotero"}], "l1gse": [{"id": "", "source": "zotero"}], "lho4h": [{"id": "", "source": "zotero"}], "nqxdl": [{"id": "", "source": "zotero"}], "pnz9d": [{"id": "", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} tags=["hermeneutics"] -->
As mentioned, it was important for us to find a method for document discovery that was guided by a research question. The research question which has guided our interest here is how the early web changed childhoods between 1995 and 2005. This is, of course, a very broad question, but it is also a good match for setting up broad, but focused topic that can be operationalised into recognisable semantic fields. Answering this question would mean looking for sites that children produced; that were targeting children; where children contributed; or where adults addressed issues related to children.

Due to limited resources, we could not test our method on all the archived web material we currently have in our possession: more than 50TB, including e.g. all archived Danish websites from between 1996 and 2006 as well as many sites in English. Instead, we wanted a smaller, more manageable corpus which we knew contained some sites that likely helped us answer our research question.

The test corpus for the method proposed here consists of archived websites from the Internet Archive. The sites chosen for the test comes from a big, manually extracted and curated corpus of URLs from printed internet guidebooks for children from the 1990s and 2000s. These sites include web pages made for or by children as well as general sites, e.g. the pages of the Louvre, discussion fora, web hotels, the White House, etc. (<cite id="jgq2b"><a href="#zotero%7C13014974%2FS7ED2JDT">(Benson &#38; Fodemski, 1999)</a></cite>,<cite id="k3526"><a href="#zotero%7C13014974%2F2GXYAT9J">(Larsen &#38; Thomsen, 1997)</a></cite>,<cite id="lho4h"><a href="#zotero%7C13014974%2FGKCQ4C2Q">(Larsen &#38; Thomsen, 1997b)</a></cite>, <cite id="84pxm"><a href="#zotero%7C13014974%2FU43GVZUX">(Larsen &#38; Thomsen, 1998)</a></cite>,<cite id="6w4po"><a href="#zotero%7C13014974%2FSY5ZK3AG">(Larsen &#38; Thomsen, 1996)</a></cite>,<cite id="6vzpx"><a href="#zotero%7C13014974%2FQ9AIA37U">(Larsen, 1998)</a></cite>).

The overall guidebook dataset currently consists of more than 3000 URLs and is a work in progress (<cite id="2nhwn"><a href="#zotero%7C13014974%2FJZSVEEYI">(Kjeldsen, 2026)</a></cite>). The initial test corpus for this article consists of a subset of 85 URLs from the overall dataset (<cite id="nqxdl"><a href="#zotero%7C13014974%2FYLMQE34P">(Kjeldsen &#38; Johnston, 2026)</a></cite>). The limit was set as we did not know how much compute time we would need for the processing when we began.

The most common way of interacting with archived websites from the Internet Archive is through their Wayback Machine, which is a URL based playback engine. The Wayback Machine can be a good entry point, when you already know which URLs you are interested in. If you don’t have this knowledge, then the archive can be difficult to explore (<cite id="7edqh"><a href="#zotero%7C13014974%2F4PZKJWL9">(Hartelius, 2020)</a></cite>). When historians are interpreting their questions and working with the archived web it can feel like looking for a needle in a haystack, without being able to grasp the size of the haystack.

The way we have retrieved material from these 85 URLS is  through a tool, which downloades resources from the Internet Archive and package the sources as WARC files (The international standard fileformat for web archive files) (<cite id="i7rhf"><a href="#zotero%7C13014974%2FVJYN5J7B">(Johnston &#38; Thøgersen, 2026)</a></cite>, <cite id="pnz9d"><a href="#zotero%7C13014974%2FWUGFM4ZU">(Maemura, 2023)</a></cite>). This method can be seen as part of one of the more computationally advanced methods of interacting with sources from the archived web. Other computational methods for working with webarchives could be to either scrape material directly or compare CDX indexes, if they are public (<cite id="art3o"><a href="#zotero%7C13014974%2F7EURECX3">(Arora et al., 2016)</a></cite>, <cite id="l1gse"><a href="#zotero%7C13014974%2FTCT6SE2I">(Nielsen et al., 2025)</a></cite>, <cite id="fo2lr"><a href="#zotero%7C13014974%2FG2LN3FW9">(Noguera et al., 2025)</a></cite>). When the archive is public, which is the case with the Internet Archive, the CDX index can be used to extract material for further analysis which is what we have done here. As mentioned above the archived web is highly fragmented. This fragmentation is also present in the corpus that we are working with (<cite id="gsghp"><a href="#zotero%7C13014974%2FYRJU2TH6">(Brügger, 2018)</a></cite>).

The resulting corpus from querying the Internet Archive for these 85 URLs with the method described above is a WARC file with 9267 resources, where 80.6% of the resources are HTML files and almost everything else are images of some kind.

<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""} tags=["hermeneutics"]
from IPython.display import Image, display
metadata={
    "jdh": {
        "module": "object",
        "object": {
            "type":"image",
            "source": [
                "Pie chart distribution of content in the first test corpus."
            ]
        }
    }
}

display(Image("./media/warc_distribution_run1.png"), metadata=metadata)
```

<!-- #region editable=true slideshow={"slide_type": ""} tags=["hermeneutics"] -->
The distribution in the pie chart above can be created for any WARC file by running the following script. It can also be found in the [WEBCHILD Github repository](https://github.com/WEB-CHILD/Scripts/blob/main/warc_content_pie.py){:target="_blank"}:
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""} tags=["hermeneutics"]
# This cell is used to define the %%skip command.
# Which makes it possible to print the script below,
# without running it in the article.
from IPython.core.magic import register_cell_magic

@register_cell_magic
def skip(line, cell):
    pass  # Do nothing

```

```python editable=true slideshow={"slide_type": ""} tags=["hermeneutics"]
%%skip # Skipping output
import warcio
from warcio.archiveiterator import ArchiveIterator
from collections import Counter
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='Plot MIME type distribution from a WARC file')
parser.add_argument('warc_file', help='Path to the input WARC or WARC.GZ file')
parser.add_argument('--output', '-o', help='Optional path to save the pie chart image (e.g., pie.png)')
parser.add_argument('--min-percent', type=float, default=1.0, help='Minimum percent threshold; types below this are grouped into "Other" (default: 1.0)')
args = parser.parse_args()

# Define colors here. Set PALETTE to either:
# - a matplotlib colormap name (string) to sample colors from, e.g. 'tab20'
# - a Python list of color strings (e.g. ['#e41a1c', '#377eb8', '#4daf4a'])
# - None to use matplotlib defaults
PALETTE = 'Pastel2'

warc_file_path = args.warc_file

# Collect MIME types
mime_types = []

with open(warc_file_path, 'rb') as stream:
    for record in ArchiveIterator(stream):
        if record.rec_type == 'response':
            content_type = record.http_headers.get_header('Content-Type')
            if content_type:
                # Some Content-Types have parameters like charset, so split them
                mime_type = content_type.split(';')[0].strip()
                mime_types.append(mime_type)

# Count occurrences of each MIME type
mime_counter = Counter(mime_types)

# Prepare data for pie chart, grouping small categories into 'Other'
total = sum(mime_counter.values())
min_pct = max(0.0, args.min_percent) / 100.0

labels = []
sizes = []
other_count = 0

for mime, count in mime_counter.most_common():
    pct = count / total if total > 0 else 0
    if pct < min_pct:
        other_count += count
    else:
        labels.append(mime)
        sizes.append(count)

if other_count > 0:
    labels.append('Other')
    sizes.append(other_count)

# Create pie chart
plt.figure(figsize=(10, 8))
# Determine colors from PALETTE defined in the file
colors = None
if PALETTE:
    if isinstance(PALETTE, (list, tuple)):
        colors = list(PALETTE)
    elif isinstance(PALETTE, str):
        try:
            cmap = plt.get_cmap(PALETTE)
            colors = [cmap(i / max(1, len(sizes) - 1)) for i in range(len(sizes))]
        except Exception:
            # If colormap lookup fails, leave colors as None to use defaults
            colors = None

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('MIME Type Distribution in WARC File')
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular
if args.output:
    plt.savefig(args.output, bbox_inches='tight')
    print(f"Saved pie chart to {args.output}")
else:
    plt.show()
```

<!-- #region citation-manager={"citations": {"64mjc": [{"id": "", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} tags=["hermeneutics"] -->
A previous paper using an LLM for classification purposes showed that the LLM performed well on markdown documents (<cite id="64mjc"><a href="#zotero%7C13014974%2FVV764MP6">(Green et al., 2024)</a></cite>). Using this insight, we converted the individual HTML files from within the WARC files to markdown files before they were given to the LLM. To ensure that we can return to the original archived file from the markdown rendered version, our conversion tool prepends each created markdown file with the URL, for transparency and to the archived version of the file can be found in the Internet Archive.

By including the archived URL in the rendered markdown and having the corpus available as a WARC file we ensure, we can access the archived source and perform a close reading of the archived site in all tools that support WARC, e.g. PyWb, SolrWayback or replayweb.page. These are all highly central tools in the webarchiving community and are built around the WARC standard. Relying on the WARC standard is important as this gives the workflow a connection to existing tools for working with sources from the archived web. Furthermore, it makes the method proposed in this article easier to apply for others working with archived web. By also choosing markdown as the input for the AI processing, it becomes applicable for scholars working with different materials than the archived web.

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["hermeneutics"] -->
## Context and category creation
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"x672j": [{"id": "", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} tags=["hermeneutics"] -->
We are interested in exploring and interpreting sources that can help us answer specific questions. To achieve a problem-driven approach to document discovery we initially created 21 topics related to our childhood history interests. These topics, the LLM uses to analyse if a given source from the corpus can provide insights into that category. They are described in individual files as the ones presented below, following Open AIs prompting strategies (<cite id="x672j"><a href="#zotero%7C13014974%2F4YGYPC4J">(Open AI, 2026)</a></cite>). The category examples below are about 1) the explicit mentioning of age, something we know is frequent in childrens' text, 2) spelling mistakes, also something we know is often present in children's writing: 

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["hermeneutics"] -->
```yaml
id: 2
name: explicit_age_child_references
description: Direct mentions of ages 5-17 or child-related terms
prompt: |
  Extract text containing age numbers 5-17, or words: "kids", "children", "boys", "girls", "børn", "barn", "dreng", "pige", "tøs", "tøser", "tøzer", "tøzzer", "tøzzzer".
  Include: "for ages", "år", "grade levels", "graders", ",5", ".5", "age", "old", "gammel"

  Do not extract numbers in relation to percentages (e.g., "5%") or ratings such as "5 stars".

  Analyze the following document and extract matching passages:
```
<!-- #endregion -->

<!-- #region editable=true raw_mimetype="" slideshow={"slide_type": ""} tags=["hermeneutics"] -->
```yaml
id: 6
name: syntactic_irregularities
description: Fragments, missing punctuation/capitalization
prompt: |
  Extract sentences that:
  - Lack capitalisation at start
  - Lack ending punctuation
  - Contain multiple punctuation marks: "!!!", "???", "!?!?"
  - Are fragments without subjects or verbs

  Analyze the following document and extract matching passages:
```

<!-- #endregion -->

<!-- #region citation-manager={"citations": {"5frso": [{"id": "", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} tags=["hermeneutics"] -->
Each topic contains a prompt for the LLM. This prompt is central to make the LLM understand what it should look for in the sources. The process of creating categories for the LLM is where domain expertise is essential. The categories for this article have been constructed from close readings of a vast number of newspapers from the period, Internet guidebooks for children, secondary literature, other media, and the archived web itself. The categories have been constructed from months of working with sources in and around the corpus. The close reading of the sources and other contextual works makes the produced categories more relevant, as we have learned through the close readings what is of interest in the corpus (<cite id="5frso"><a href="#zotero%7C13014974%2F4T525T4G">(Ohrvik, 2024)</a></cite>). Additionally, some of the categories have been enhanced with informal knowledge from lived experience.[^1](#note1)
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["hermeneutics"] -->
## Building document-level binary classifications through inference
<!-- #endregion -->

<!-- #region editable=true jp-MarkdownHeadingCollapsed=true slideshow={"slide_type": ""} tags=["hermeneutics"] -->
Retrieval Augmented Generation (RAG) operates by embedding document chunks into vector space and retrieving those most similar to a query. For the present task, this approach is unsuitable: we know our categories, but we do not know the language used by children of the era across two different languages and cultures. Embedding-based similarity would impose a contemporary model's latent associations onto a corpus where the vocabulary of interest is historically and culturally situated. A 2025-trained model cannot predict what words a Danish child would have used on the internet in 1997. We require a method that applies our categories exhaustively to every document without relying on the model's notion of relevance.

Drawing on database indexing techniques, Ballsun-Stanton proposed building a binary index: a presence/absence classification per document per category, enabling faceted search by deductively identified concepts rather than retrieval by vector similarity. The genesis of this approach was OpenAI's publication of GPT-OSS-Safeguard (https://huggingface.co/openai/gpt-oss-safeguard-120b), an open-weight model that classifies incoming text against developer-defined policies. The same architecture applied to the parent GPT-OSS model could power a classifier based on researcher-defined categories rather than safety policies, drawing on established approaches in multiclass text classification (<cite id="d14sm"><a href="#zotero%7C13014974%2FSY4XQWST">(Walsh &#38; Greaney, 2025)</a></cite>). Huskey (<cite id="4kn4j"><a href="#zotero%7C13014974%2F9JDELNNG">(Huskey, 2025)</a></cite>) demonstrates a comparable pattern in digital humanities: using fine-tuned language models as cost-effective instruments for tedious classification tasks that would otherwise create bottlenecks in the research pipeline.

Rather than filtering or ranking documents by estimated relevance, we generated a full Cartesian product of classifications: every document evaluated against every category. Documented absence is as informative as presence, as a faceted search may both usefully include and exclude items. The task given to the model is narrow in scope: deductively determine whether the document presented matches or does not match the category presented. We constrained all opportunities for the model to apply judgement beyond this scope: no ranking of matches, no interpreting our search terms into associations the model might project onto historical vocabulary. The model provides a search-enabled interface; the researchers do the research.

This approach reprises the deductive content analysis methodology of Elo and Kyngäs (<cite id="9wzfn"><a href="#zotero%7C13014974%2FDBZ9K4WT">(Elo &#38; Kyngäs, 2008)</a></cite>), in which a categorisation matrix constructed from prior theoretical knowledge is applied systematically to a body of text. The model is constrained by a system prompt that defines its role:
```
You are a text extraction tool for historical web research. You extract verbatim blockquotes from 1996-2005 web pages that contain specific linguistic or structural features.

You make no interpretive judgments about intent or audience. You only identify and extract text containing specified patterns.

Each classification call pairs one document with one category prompt and requires a structured response: 

First, provide your reasoning and analysis. Then, provide ONLY valid JSON with this structure: { "match": "yes" or "maybe" or "no", "blockquotes": ["quote 1", "quote 2"] }
```

Requiring reasoning before the verdict is deliberate. By forcing the model to articulate its interpretation of the category before committing to a classification, we produce internal consistency between the analysis and the output using a "Thought Anchor" pattern (<cite id="8cbzy"><a href="#zotero%7C13014974%2F56FTR44T">(Bogdan et al., 2025)</a></cite>). This is distinct from chain-of-thought prompting for problem-solving: the reasoning exists to bind the model to a coherent position, not to discover one. The reasoning traces are preserved in the database, serving additionally as an audit trail and as a means of prompt calibration. We read how the model interpreted category boundaries and refine prompts accordingly. All inference was performed at temperature 0 for deterministic, reproducible classifications.

The result is a corpus where every document-category pair has a definitive classification. The extracted blockquotes enable a further step: researchers may make an inductive coding pass on the extracted evidence to support the research question under investigation, building on the deductive scaffold.

We used OpenAI's GPT-OSS-120b (<cite id="jmbps"><a href="#zotero%7C13014974%2F8LDGEYHZ">(OpenAI, 2025)</a></cite>), a Mixture of Experts model with 117 billion total parameters and 5.1 billion active parameters per inference, released under the Apache 2.0 licence. The model was self-hosted: the ethics protocols governing the corpus do not permit data to leave university infrastructure. We used the UCloud interactive HPC system, managed by the eScience Centre at the University of Southern Denmark, running the model via vLLM (<cite id="qrojs"><a href="#zotero%7C13014974%2FX4KMF56X">(Kwon et al., 2023)</a></cite>) on a compute node with two NVIDIA H100 GPUs in a tensor-parallel configuration. The Kidlink corpus required approximately 300 GPU-hours across multiple sessions in early February 2026. Had an external provider been permissible, the exhaustive classification would have required approximately 15 billion input tokens, at an estimated cost of US$650 against GPT-OSS-120b on DeepInfra (23 March 2026, OpenRouter pricing).

The corpus contains content in English and Danish. GPT-OSS-120b is English-dominant, and classification quality drops for other languages. To mitigate this, category prompts include explicit target terms in Danish — for example, category 02 lists "børn", "barn", "dreng", and "pige" alongside English equivalents. This provides lexical scaffolding that reduces the inferential burden on the model for non-English content. We do not claim good cross-lingual model understanding; this is a best-effort extension of an English-optimised approach.

The processing architecture evolved iteratively through three approaches. An initial integration with the vLLM Python API proved unreliable. Batch processing followed, but produced opaque failures later traced to binary content and oversized documents corrupting batches. This is a good example of how messy a source the archived web is. The final architecture uses vLLM as an OpenAI-compatible HTTP server, with a pool of 384 worker threads issuing individual requests. These threads consume pairwise category-documents and emit them to a JSONL log, allowing for debugging and processing retries on individual document-category pairs. The worker concurrency level was determined through empirical benchmarking to saturate the GPU batch capacity on this infrastructure. We found that there was no need to reserve headroom. Key-value caches were best utilised with one worker per vLLM thread.

Crash resilience was a hard operational requirement, not defensive engineering. HPC allocations on UCloud begin with a one-hour walltime and must be manually extended in increments while the machine is running. If the allocation expired, the machine would perform a hard shutdown with no graceful termination signal. The pipeline was therefore designed to survive abrupt power loss: results are written atomically using a temporary-file-then-rename pattern (atomic on POSIX filesystems), and any completed classification that reaches disk survives. On the next allocation, the pipeline resumes from where it stopped. An early attempt to use SQLite's Write-Ahead Logging (WAL) in conjunction with Syncthing for file synchronisation produced corrupted databases, as WAL mode assumes single-filesystem locking semantics. Results were instead written as individual JSON files and imported to SQLite locally after being batched into a JSONL. Documents exceeding 80,000 characters were split at natural boundaries (headings, paragraph breaks) with a 500-character overlap for context continuity. Split parts were processed independently, with results aggregated at the document level: if any part matched, the document was classified as matching. The markdown corpus also contained unconverted binary files (archives, executables, images, and Flash objects), which were detected by file header signatures and excluded before processing.

Correctness of the classifications was established through iterative prompt calibration. Results from an initial run were sampled, and domain experts audited the classifications against source documents. Where the model's judgements diverged from expert assessment, category prompts were refined, and the corpus reprocessed. The 20b variant of GPT-OSS was used for development iteration; all published results were produced with the 120b model, which adhered closely enough to the refined prompts that further calibration was not required at scale. All code for the classification can be found in the [LLM Document Discovery repository](https://github.com/WEB-CHILD/LLM-Document-Discovery){:target="_blank"}
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
## Results of first iterations
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"bd7y9": [{"id": "", "source": "zotero"}], "edocn": [{"id": "", "source": "zotero"}], "yukfn": [{"id": "", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
All LLM computation for this project was performed on the UCloud interactive HPC system, which is managed by the eScience Center at the University of Southern Denmark. In this HPC setup we had access to a compute node with two H100 GPUs for 500 hours. We used approximately 100 compute hours in development and approximately 300 to generate this corpus. The computation resulted in more than 130,000 matches between documents and different categories. These category matches were all stored in a local database.

After the first run we performed a quality check of the results by sampling ten results for each category adding up to 210 individual documents. These documents were reviewed manually, and the LLM’s reasoning for including them was compared with our close reading. From these samples, it became clear that some categories performed better than others. For instance, initially, we had a category matching  imperative commands directed at the reader, but this extracted many unwanted results. In one case, a Terms of Agreement site from Paramount was put into this category, but it does not nudge the user to interact (<cite id="yukfn"><a href="#zotero%7C13014974%2FVMLLQHSC">(Paramount, 1997)</a></cite>). Other categories performed remarkably better. An example of a well performing category is the category that extracts age identity claims. This category successfully extracted text where children declared their ages (<cite id="edocn"><a href="#zotero%7C13014974%2FULATUTGL">(<i>One Fine Day</i>, 1997)</a></cite>). After the first run categories that did not provide value were removed, while other categories were enhanced to perform better, often when the LLM matched exactly what it had been instructed to, but where the instruction had not been properly demarcated by the authors. An example would be the category related to colour schemes, which was changed from linguistic descriptions of colour to technical descriptions of colour in the source code.

The individual categories often return a multitude of matches. The real value of the categorisation becomes clear when documents matching multiple categories at once are extracted. In our case we were particularly interested in discovering parts of the web where children were visibly present and active. This could usefully and reliably be extracted by our categories that matched non-standard spelling, age identity claims, and informal youth slang. By querying the database of results for documents that match on all three categories at once, we get 22 results out of the 130.000 in total. 22 results are easily close read but they do not constitute a comprehensive set of sources. To reach a richer and more wide-ranging set of sources different categories must be combined. When results combining categories are close read, it is clear that they were written by children. This approach will be discussed further in the following section, where the method was applied on the bigger Kidlink corpus introduced above.

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
## Results of last iteration
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
As mentioned in the beginning of the [Corpus](#Corpus)-section, the methodology developed has been applied to a corpus consisting of all archived material from the kidlink.org material available at Internet Archive. This corpus consists of more than 380 thousand sources where almost 300 thousand of these are text. For this iteration, we ran the LLM with our updated categories for an extended amount of time on the HPC infrastructure.
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
from IPython.display import Image, display

metadata={
    "jdh": {
        "module": "object",
        "object": {
            "type":"image",
            "source": [
                "Pie chart distribution of content in the Kidlink corpus."
            ]
        }
    }
}

display(Image("./media/warc_distribution_run2_kidlink.png"), metadata=metadata)
```

<!-- #region editable=true slideshow={"slide_type": ""} -->
Running the method on this many documents produced a database with more than five million matches between categories and sources. This number of results requires us to match sources on multiple categories at once. This is done to narrow the number of results, but also to zoom in on documents that can be used to investigate the questions that we are interested in as researchers. As an example, we will be focusing on discovering sources that can inform us on how children communicated with others on the Kidlink forum before 2005.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["hermeneutics"] -->
When working with results of this magnitude, we need to filter the results meaningfully to answer our questions. In this approach, we are filtering for sources that match multiple categories we have deemed interesting when combined. For instance, we were interested in sources that matched the following five categories at once: 

| Category name                 | Description |
|-------------------------------|-------------|
| explicit_age_child_references | Direct mentions of ages 5-17 or child-related terms|
| non_standard_spelling         | Phonetic spellings, number substitutions, repeated letters|
| topic_mixing_markers          | Sudden topic shifts within single passages|
| age_identity_claims           | Self-reported ages, grade references|
| youth_slang_informality       | Informal expressions, slang, emoticons|

As the results from the LLMs categorisation are stored in a SQLite database, it is possible to computationally extract all sources that match all of the categories above with the following python script:
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""} tags=["hermeneutics"]
#!/usr/bin/env python3
"""
multiple_category_matcher.py

Finds results that match ALL of the specified categories in a SQLite database.

Usage:
    python multiple_category_matcher.py <db_path> --categories <id1> <id2> ...

Example:
    python multiple_category_matcher.py results.db --categories 1 4 6 7 11
"""

import argparse
import sqlite3
import sys


def fetch_matched_results(db_path: str, category_ids: list[int]) -> list[sqlite3.Row]:
    """
    Query the SQLite database for results that match ALL of the given category IDs.

    Args:
        db_path:      Path to the SQLite database file.
        category_ids: List of category IDs that must all be matched.

    Returns:
        A list of sqlite3.Row objects with columns:
            - result_id          (int)
            - content            (str)
            - matched_categories (str, comma-separated category names)
    """
    setup_query = """
        DROP TABLE IF EXISTS wanted_categories;

        CREATE TEMP TABLE wanted_categories (
            category_id INTEGER PRIMARY KEY
        );
    """

    main_query = """
        WITH matched_results AS (
            SELECT
                rc.result_id
            FROM result_category rc
            WHERE rc.match = 'yes'
              AND rc.category_id IN (
                  SELECT category_id FROM wanted_categories
              )
            GROUP BY rc.result_id
            HAVING COUNT(DISTINCT rc.category_id) =
                   (SELECT COUNT(*) FROM wanted_categories)
        )
        SELECT
            r.result_id,
            r.content,
            GROUP_CONCAT(c.category_name, ', ') AS matched_categories
        FROM matched_results m
        JOIN result r
          ON r.result_id = m.result_id
        JOIN result_category rc
          ON rc.result_id = m.result_id
        JOIN category c
          ON c.category_id = rc.category_id
        WHERE rc.match = 'yes'
          AND rc.category_id IN (
              SELECT category_id FROM wanted_categories
          )
        GROUP BY
            r.result_id,
            r.content
    """

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        conn.executescript(setup_query)
        conn.executemany(
            "INSERT INTO wanted_categories (category_id) VALUES (?)",
            [(cid,) for cid in category_ids],
        )
        cursor = conn.execute(main_query)
        return cursor.fetchall()


def print_table(rows: list[sqlite3.Row]) -> None:
    """
    Print query results in a human-readable card layout.

    Each result is rendered as a card showing the result ID, matched category
    names, and the first three non-empty lines of the content field.
    A final summary line reports the total number of rows returned.

    Args:
        rows: List of sqlite3.Row objects as returned by fetch_matched_results.
    """
    if not rows:
        print("No results found.")
        return

    width = 80
    divider = "=" * width
    thin = "-" * width

    for row in rows:
        content_preview = "\n".join(
            f"  {line}" for line in str(row["content"]).splitlines()[:3] if line.strip()
        )

        print(divider)
        print(f"  Result ID : {row['result_id']}")
        print(f"  Categories: {row['matched_categories']}")
        print(thin)
        print(content_preview)

    print(divider)
    print(f"{len(rows)} row(s) returned.")


def main() -> None:
    """
    Entry point for the command-line interface.

    Parses arguments (db_path and --categories), calls fetch_matched_results,
    and prints the results via print_table. Exits with code 1 on database
    errors.
    """
    parser = argparse.ArgumentParser(
        description="Find results matching ALL specified categories in a SQLite DB."
    )
    parser.add_argument("db_path", help="Path to the SQLite database file")
    parser.add_argument(
        "--categories",
        nargs="+",
        type=int,
        required=True,
        metavar="ID",
        help="One or more category IDs that must ALL match",
    )
    args = parser.parse_args()

    try:
        rows = fetch_matched_results(args.db_path, args.categories)
        print_table(rows)
    except sqlite3.OperationalError as e:
        print(f"Database error: {e}", file=sys.stderr)
        sys.exit(1)

# Out comment when run as a standalone script
# if __name__ == "__main__":
#     main()

```

<!-- #region editable=true slideshow={"slide_type": ""} tags=["hermeneutics"] -->
The script can be called from the command line, or its methods can be imported as done below. The example included as part of this article uses the initial test corpus introduced above, consisting of approximately 9000 sources. The categories 2, 5, 7, 8 and 13 are the five in the table above. The results of the example below come from the domains kidpub.org or kidlink.org.

When the extraction script was run on the bigger Kidlink corpus, 428 sources were extracted. Among these 428 sources, we have found sources that we have not been able to locate through traditional close reading of the corpus, as it has not been possible to discover them through traditional search interfaces or by navigating the sources in a web archive.
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""} tags=["hermeneutics", "table-1"]
from script.multiple_category_matcher import fetch_matched_results, build_dataframe
from IPython.display import display, HTML
import pandas as pd

pd.set_option('display.max_colwidth', 100) 


categories_to_match = [2, 5, 7, 8, 13]
matching_results = fetch_matched_results("./script/first_corpus_120b.db", categories_to_match)

df = build_dataframe(matching_results)

df
```

<!-- #region editable=true slideshow={"slide_type": ""} -->
As mentioned in the section above the approach has made it possible for us to discover sources from situations where children are interacting differently than was the case in other parts of the Kidlink domain. By categorising each source from the Kidlink domain into our categories we have been able to find material that we did not know existed on the domain. Without an exploratory approach such as the one used here sources that were not easily available through navigation would most likely never have been discovered.

One example of such a source is a log from an Internet Relay Chat, which we have only been able to discover through this approach. The landing page of kidlink.org has has a consistent design throughout our period. From the landing page users would be introduced to how they were supposed to participate in Kidlink and they would be guided towards specific parts of the domain. When exploring the archived versions of the domain with the landing page as a starting point, one is left with a one sided narative of primarily educational content. The LLM assisted discovery of source material changes what can be found. By querying our database of categorised sources we were able to find a log from an IRC event, otherwise deeply buried in the sites structure. In this IRC children were chatting with a Bosnian girl who kept a diary during the Bosnian War. This form of direct communication have been almost impossible to find when navigating from the landing page.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
## Scalability, usability and ethics
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"0n6cm": [{"id": "", "source": "zotero"}], "blxsm": [{"id": "", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
We had 500 hours of HPC allocated for developing the methodology. This amount of HPC has been sufficient for developing the approach. In its current state, the methodology does require a substantial amount of computing power. The following section introduces some challenges and thoughts about how the method can be applied to other corpora and how computing times can be kept down.

During our first run of the method on the initial small test corpus, we spent 81 computing hours with the GPT-OSS-20B model. Our compute times were  significantly reduced by optimisations introduced before a second run, making it feasible to run the larger model GPT-OSS-120B. In fact, the current setup processed our initial test corpus of sources in exactly two hours with the larger GPT-OSS-120B. When we applied the method to our bigger Kidlink corpus, the computation times were higher. Bigger compute times for bigger corpora are not issues in themselves; they, however, emphasise the need for the construction of well-performing categories through test runs on a smaller corpus, before analysing bigger corpora.

The methodology proposed in this article is suitable for working with smaller corpora of archived web material. Two considerations inform why this is the case. Firstly, we have a concern about scalability, and secondly, there is an ethical dimension that needs to be addressed.

As the proposed method is iterating on the individual documents multiple times, we see a potential issue working with corpora that are of terabytes in size. In our test study above, we ended up with 21 categories, which translates to 21 iterations on each document in the corpus. If one were to define ten categories only, the computation times would effectively be cut in half and so on. 

An example of a larger-scale investigation could be running the method on all the archived web pages from the Danish national web archive from 1995-2005, a corpus comprising 500 million sources. Our first corpus, the nine thousand sources, is only a tiny fraction compared to the material collected in the WEBCHILD project.

<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
# Calculation of how big a part of the source material the initial test corpus consists of. 
test_corpus = 9000 # amount of documents
total_corpus =500000000 # total amount of sources

fraction = test_corpus / total_corpus 
percentage_of_total = fraction * 100
percentage_of_total
```

<!-- #region editable=true slideshow={"slide_type": ""} -->
Assuming that the code implementation scales linearly, the classification would need to run 55.556 times longer, resulting in more than twelve years of computing time in a powerful HPC environment. However, this does not mean that the approach cannot be applied at scale. Large-scale implementations would need to think of ways to bring down compute time by either defining fewer and maybe broader categories or using a smaller but still well-performing language model. As researchers, we have a responsibility to make our approaches as efficient as possible for the sake of the environment (<cite id="blxsm"><a href="#zotero%7C13014974%2FDSGN2HJL">(Tamburrini, 2022)</a></cite>). This can be done by either changing some of the parameters for the approach as discussed here. Another approach could be to ensure that the chosen HPC institution relies on green energy sources and uses energy-efficient hardware for the clusters.

Another important environmental consideration is the AI carbon footprint. Concerns relating to AI carbon footprint are often concentrated on the environmental impact of training AI systems (<cite id="0n6cm"><a href="#zotero%7C13014974%2FJMGXMZ79">(He et al., 2025)</a></cite>). However, other reports and articles find that up to 90% of emissions from AI are related to how the systems are used after training (<cite id="blxsm"><a href="#zotero%7C13014974%2FDSGN2HJL">(Tamburrini, 2022)</a></cite>). Kate Crawford has done exhaustive work on how uses of AI should always be seen in a broader environmental context. She speaks of AI as a megamachine drawing on Lewis Mumfords framework: "Artificial intelligence is another kind of megamachine, a set of technological approaches that depends on industrial infrastructures, supply chains, and human labor that stretch around the globe but are kept opaque." (<cite id="yah3e"><a href="#zotero%7C13014974%2FCSKJCUV2">(Crawford, 2021)</a></cite>, 48). Implementing AI solutions should take these impacts into account.

There are definitely challenges involved when applying our proposed approach at a larger scale. This approach could contribute substantially to the carbon footprint from using AI if applied uncritically at scale. However, this does not mean that the approach cannot produce meaningful results. In fact, as we have demonstrated, the method does a good job at narrowing material for close reading.

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
# Conclusion: document discovery as an alternative to traditional search
<!-- #endregion -->

Earlier research by Bell et al. showed a great need for alternative approaches to document discovery in web archives due to their vast nature and complicated provenance (<cite id="8dxoz"><a href="#zotero%7C13014974%2FU4NRYK6X">(Bell et al., 2022)</a></cite>). The method for document discovery outlined in this article has shown both productive and sound results. Tested first on a smaller set of sources (9267) and followed by a large corpus (380.000), we were able to discover websites were kids were visibly present and interacting across both. The way the LLM is used in our document discovery aims at handling one of the biggest challenges in using this technology for research that needs to be both transparent and precise. By having the LLM provide us with quotes from the sources and detailed reasoning why these were chosen as well as the URL of the source, we were able to triple-check the validity of the output. The direct link back to the source enabled us to manually check the model's reasoning and consider if we agreed. Furthermore, the quotes were computationally checked against the source to ensure that they did, in fact, appear on the site. This way of reigning in the probabilistic flaws of the LLM proved useful as we found no signs of so-called hallucination.

As discussed above the method has ethical problems in terms of resources when used at scale. The individual researcher must consider whether the purpose of the research justifies any large-scale use. Small-scale studies as for instance the 380 thousand-item Kidlink corpus is better suited for this method. We could see a future use in smaller web archives where certain collections are of interest to a larger research community, like the UK Web Archive or special collections at the International Internet Preservation Consortium. In these collections, researchers might have overlapping interests and could therefore reuse some of the previous document discoveries.



<!-- #region editable=true slideshow={"slide_type": ""} -->
# Notes
<!-- #endregion -->

<!-- #region citation-manager={"citations": {"94l0n": [{"id": "", "source": "zotero"}]}} editable=true slideshow={"slide_type": ""} -->
[1](#note1): As two of the authors were children in the period that the article is interested in, examples from their childhood were included when constructing the categories. This resembles a postphenomenological approach to using one’s own lived experience. For examples, see: <cite id="94l0n"><a href="#zotero%7C13014974%2F2S7NF3RT">(Ihde, 2010)</a></cite>
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} tags=["hidden"] -->

<!-- #endregion -->
