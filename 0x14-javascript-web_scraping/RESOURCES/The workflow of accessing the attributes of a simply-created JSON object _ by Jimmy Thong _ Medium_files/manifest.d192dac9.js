(()=>{"use strict";var e,t,n,a,o={},i={};function c(e){if(i[e])return i[e].exports;var t=i[e]={id:e,loaded:!1,exports:{}};return o[e].call(t.exports,t,t.exports,c),t.loaded=!0,t.exports}c.m=o,c.x=e=>{},c.amdO={},c.n=e=>{var t=e&&e.__esModule?()=>e.default:()=>e;return c.d(t,{a:t}),t},t=Object.getPrototypeOf?e=>Object.getPrototypeOf(e):e=>e.__proto__,c.t=function(n,a){if(1&a&&(n=this(n)),8&a)return n;if("object"==typeof n&&n){if(4&a&&n.__esModule)return n;if(16&a&&"function"==typeof n.then)return n}var o=Object.create(null);c.r(o);var i={};e=e||[null,t({}),t([]),t(t)];for(var r=2&a&&n;"object"==typeof r&&!~e.indexOf(r);r=t(r))Object.getOwnPropertyNames(r).forEach((e=>i[e]=()=>n[e]));return i.default=()=>n,c.d(o,i),o},c.d=(e,t)=>{for(var n in t)c.o(t,n)&&!c.o(e,n)&&Object.defineProperty(e,n,{enumerable:!0,get:t[n]})},c.f={},c.e=e=>Promise.all(Object.keys(c.f).reduce(((t,n)=>(c.f[n](e,t),t)),[])),c.u=e=>"static/js/"+({118:"instrumentation",192:"PublicationFollowersPage.MainContent",214:"NotificationsPage.RightColumnContent",261:"SeriesPage.MainContent",315:"LandingGiftPage.MainContent",445:"MastodonForMembersPage.MainContent",608:"CustomizeFollowingPage.MainContent",679:"CustomizeReadingHistoryPage.MainContent",716:"UserFollowingPage.MainContent",899:"UserCatalogPage.MainContent",903:"PartnerProgramUnenrollPage.MainContent",1050:"GroupGiftMembershipPage.MainContent",1165:"PublicationDigestStatsPage.MainContent",1178:"StatsHomepagePage.MainContent",1186:"ThreadedCatalogResponsesSidebar",1234:"TheTrump45Page.MainContent",1245:"CommunityPublicationFeaturePage.MainContent",1252:"UpdatePaymentPage.MainContent",1388:"dev",1572:"CommunityPublicationStatsPage.MainContent",1727:"YourCatalogsPage.RightColumnContent",1826:"LOHomeAnimation",1834:"PublicationFollowersPage.RightColumnContent",1865:"GlobalUnsubscribeNewslettersPage.RightColumnContent",1904:"CommunityPublicationFeatureSectionPage.MainContent",1916:"PaypalButton",2080:"HomePage.RightColumnContent",2129:"YourFollowedCatalogsPage.RightColumnContent",2213:"SearchPage.RightColumnContent",2255:"CustomizeSuggestionsPage.RightColumnContent",2267:"HomeLoPage.MainContent",2270:"CommunityPublicationAboutPage.MainContent",2280:"SettingsPage.RightColumnContent",2337:"SignInPage.MainContent",2373:"YourStoriesPage.RightColumnContent",2422:"OnboardingPlansPage.MainContent",2427:"PublicationNewsletterLandingPage.MainContent",2614:"PublicationProfilePage.MainContent",2672:"NotificationSettings",2791:"UserProfilePage.MainContent",2831:"CustomizeMutedPage.MainContent",2855:"PublishingSettings",3050:"UserFollowingPage.RightColumnContent",3144:"PartnerProgramStripeReconnectPage.MainContent",3195:"YourFollowedCatalogsPage.MainContent",3295:"CustomizeFollowingPage.RightColumnContent",3350:"TopicPortalPage.MainContent",3413:"PublicationTaggedPage.RightColumnContent",3419:"MobileWebEditorRedirectPage.MainContent",3692:"YourStoriesPage.MainContent",3769:"PlansPage.MainContent",3774:"UnrecognizedAccountPage.MainContent",3802:"CustomizeMutedPage.RightColumnContent",3965:"YourReadingHistoryPage.RightColumnContent",4009:"MastodonCallbackPage.MainContent",4124:"CrupdatePasswordPage.MainContent",4212:"SettingsCustomDomainPage.MainContent",4310:"TopicWhoToFollowPage.MainContent",4445:"HomeLoLegacyPage.MainContent",4593:"PublicationDesignEditorPage.MainContent",4657:"SettingsPage.MainContent",4729:"InternalStatusPage.MainContent",4790:"PublicationProfilePage.RightColumnContent",4863:"WriterSubscriptionPromotionPage.MainContent",4894:"TagArchivePage.MainContent",5085:"UserCatalogPage.RightColumnContent",5160:"YourCatalogPage.MainContent",5232:"LegacyTopicRedirectPage.MainContent",5284:"UserCatalogsPage.RightColumnContent",5317:"TicksPage.MainContent",5344:"react-select",5464:"EmbedCatalogPage.MainContent",5509:"YourCatalogsPage.MainContent",5531:"PostPage.MainContent",5587:"TopicsOnboardingPage.MainContent",5620:"CustomizeReadingHistoryPage.RightColumnContent",5736:"PublicationAboutPage.MainContent",5841:"CancelMembershipPage.MainContent",5849:"YourCatalogPage.RightColumnContent",5872:"CommunityPublicationNewsletterPromotionPage.MainContent",5881:"ImportMailingListPage.MainContent",5963:"LandingPartnerProgramPage.MainContent",5974:"UserCatalogsPage.MainContent",6029:"UserFollowersPage.MainContent",6035:"PublicationAboutPage.RightColumnContent",6205:"UserBooksPage.MainContent",6329:"SecuritySettings",6333:"AccountSettings",6391:"SpeechifyWidget",6476:"ManageMembershipPage.MainContent",6635:"responses.editor",6648:"PublicationTaggedPage.MainContent",6662:"PublicationNewsletterPromotionPage.MainContent",6908:"ShareSuccessPage.MainContent",6991:"YourReadingHistoryPage.MainContent",7039:"CommunityPublicationTrendingPage.MainContent",7097:"PartnerProgramDashboardPage.MainContent",7181:"PublicationNewsletterSettingsPage.MainContent",7210:"GlobalUnsubscribeNewslettersPage.MainContent",7252:"SearchPage.MainContent",7253:"CommunityPublicationProfilePage.MainContent",7638:"PartnerProgramStripeFinishPage.MainContent",7642:"UserBooksPage.RightColumnContent",7660:"CustomizeSuggestionsPage.MainContent",7757:"StatsPostPage.MainContent",7830:"LandingAboutPage.MainContent",8014:"SubscriptionStatsPage.MainContent",8249:"TopicRecommendedPage.MainContent",8328:"LandingVerifiedAuthorsPage.MainContent",8490:"UserDesignEditorPage.MainContent",8636:"RedeemGiftMembershipPage.MainContent",8711:"PartnerProgramStripeReconnectSuccessPage.MainContent",8763:"Devtool",8837:"GiftMembershipPage.MainContent",8857:"BillingReceiptPage.MainContent",8913:"ThreadedResponsesSidebarContent",8916:"UserProfilePage.RightColumnContent",8954:"LandingMembershipPage.MainContent",8986:"CommunityPublicationTaggedPage.MainContent",9076:"GiveTipButton",9128:"RedeemGiftMembershipModal",9143:"CommunityPublicationArchivePage.MainContent",9152:"reporting",9267:"NotificationsPage.MainContent",9293:"WelcomeMemberPage.MainContent",9383:"hatch",9449:"LandingB2BPage.MainContent",9453:"PostSettingsPage.MainContent",9456:"CollectionsLibraryPage.MainContent",9501:"CommunityPublicationLatestPage.MainContent",9534:"UserAboutPage.RightColumnContent",9558:"ExploreTopicsPage.MainContent",9627:"MembershipSettings",9655:"NotAvailablePage.MainContent",9686:"DiscountPlansPage.MainContent",9690:"HomePage.MainContent",9789:"UserAboutPage.MainContent",9827:"PartnerProgramApplicationPage.MainContent",9862:"PublicationCustomDomainSettingsPage.MainContent",9868:"UserFollowersPage.RightColumnContent",9985:"TributePage.MainContent"}[e]||e)+"."+{118:"5e7f2981",192:"689e9b0b",209:"6b046446",214:"39951159",261:"468b9032",315:"ee2fe6d2",372:"4bc3db2a",445:"1671fc34",455:"1a1c5010",466:"c3deb54d",500:"80a4127d",513:"f19d666c",543:"9e361d4c",608:"aa2a32c2",621:"6ff9c479",679:"8578f31e",705:"da9267d6",716:"72acdd3f",722:"7f177055",773:"899467eb",803:"b1baa49a",836:"6e7aa622",899:"0d13fea1",903:"ca6012a3",1050:"f079bba6",1165:"1fd83de2",1178:"73a27dfb",1186:"b7f32383",1234:"feb0b7e7",1245:"cc1cf733",1248:"a53b8cc8",1252:"0589ba34",1388:"7d560992",1455:"00508433",1488:"553173cf",1572:"5e8468f1",1689:"cf9af42c",1711:"b70f1a35",1727:"ee23fd65",1730:"2c8b907c",1826:"d6dfa4cf",1834:"bdad8524",1865:"aef9ea3a",1878:"73a360f3",1904:"066a7070",1916:"d060584b",1937:"75389df3",2063:"25f3a769",2064:"6ab53062",2080:"51719606",2129:"23da2137",2212:"8ba54f97",2213:"19375fcf",2230:"c546f16c",2255:"66cc75fe",2267:"43e21240",2270:"b31689cb",2280:"9603a4d0",2331:"6c1b222a",2337:"52f6ae0e",2373:"fcc3ca9e",2400:"223e0f81",2422:"dc54ed55",2427:"18443040",2485:"451ba18b",2562:"861649bc",2605:"3e4d3977",2614:"83b26360",2672:"65c36592",2791:"18ae236b",2794:"8c5a9056",2831:"f7eb6971",2851:"cf02744b",2855:"d4f87931",2979:"065bc08e",3050:"2b31432c",3144:"e982d825",3192:"3e429179",3195:"39851e00",3295:"78f3c74a",3350:"37190fb7",3371:"423e37a8",3383:"39e61d55",3413:"79a7670f",3419:"32d0e9a7",3547:"cf99eb0e",3581:"10bfab4a",3587:"e8d17f9f",3652:"08f3defe",3692:"55238d15",3695:"935076c1",3763:"9820eb6b",3769:"6f757856",3774:"a63ab910",3802:"110bdccc",3824:"1df15824",3849:"b7e2168f",3891:"839511d9",3952:"5e1b2ced",3959:"eea18434",3965:"bde8277e",4009:"a6800d6e",4042:"91470544",4124:"12a51e3e",4209:"6ba88fd6",4212:"c7183bdd",4294:"e24d8924",4310:"e45e2ffc",4332:"49763622",4341:"e697d2a1",4398:"db4d4378",4445:"7de8229b",4447:"522494b1",4483:"2230bcf4",4593:"8d6e2b7a",4657:"5f3d2964",4667:"993ebc2b",4729:"5606ddca",4736:"87f769af",4790:"3104ab09",4863:"3684ad9e",4884:"8bbee0da",4894:"a3418531",4897:"f4f96559",4909:"f2dedd14",4911:"06a852d8",5085:"a394d020",5160:"9bfbcb11",5177:"1b7b6432",5181:"8da8aec5",5186:"a11b2bb9",5203:"e7a22052",5232:"1abf089e",5249:"c757fed8",5251:"e4fcb9a8",5284:"129daa4d",5317:"704f63b7",5344:"d8628178",5384:"bfdedcab",5464:"374f07d1",5472:"778c8cb3",5509:"e1898edf",5514:"6018be2b",5531:"12f09e15",5587:"a1463a12",5601:"115530e6",5620:"20a47c36",5631:"363b8e36",5699:"f58c4262",5700:"1c9f05c6",5736:"24de799a",5781:"39279ff8",5831:"b4c0b921",5841:"04742f2b",5849:"79ffaf27",5872:"a2130400",5881:"2446e295",5963:"a08c38b9",5964:"0a1b3d70",5971:"fd9e1c6f",5974:"18d5b1ee",6029:"746c49b4",6035:"644c1727",6046:"f9be485b",6068:"e9093f2e",6091:"3d368674",6156:"57448690",6159:"2896e66f",6205:"4ff3493f",6318:"b05a590e",6329:"4fc8becd",6333:"6ff70df8",6358:"a78f5809",6391:"84ab8259",6476:"888044fb",6481:"e3e8b67f",6605:"caa5db7b",6635:"b352478b",6637:"8a411a8c",6648:"c6ab00ce",6662:"e7f4fc39",6880:"dbbaa0f7",6908:"62dc5050",6917:"db917a5e",6991:"670a0540",7039:"47714416",7084:"485eb979",7097:"3fae954f",7098:"7bbb418a",7111:"1421aaa2",7118:"9138b7ec",7131:"748f3ddd",7136:"50c74aec",7181:"0f366d7d",7210:"a4df62f2",7225:"ad71ba28",7252:"dcffe6a7",7253:"1ce200a0",7288:"29e1de80",7360:"e26d33fa",7413:"54741f0b",7440:"0a9055e3",7603:"4fe0cd15",7638:"157044ed",7642:"da58d588",7660:"21ecdcf6",7676:"ad6b1f0f",7749:"bd29ceb9",7757:"525f35e4",7794:"aa3da6b3",7830:"7dcea956",7883:"0e445e04",7906:"47ff48f1",7915:"a86e2090",8014:"7278b1d7",8022:"253cf0dc",8052:"60aa38b6",8069:"ba53a61f",8097:"afb6fd3b",8239:"c5456e5e",8249:"1dfcb7cc",8328:"22811a33",8410:"3a007b36",8447:"49ac73d8",8490:"e362bf62",8491:"7fa46461",8501:"2a38ae01",8557:"782c1470",8565:"ce53d42b",8577:"ee8f00bd",8580:"feeb2549",8597:"31012efa",8636:"7567ef46",8695:"17d1af21",8711:"3daa6292",8763:"d1f40854",8837:"3f4988de",8857:"7a59e854",8883:"c8b03d13",8913:"d096a4a6",8916:"d379bc91",8954:"dddec6be",8981:"7d311ff9",8986:"1b74c728",9012:"314f1cf2",9052:"a05296d6",9066:"5415772e",9076:"7844a2d2",9128:"b7bb19ab",9143:"833912dc",9152:"2021fe63",9174:"24f568ee",9207:"f057f7ef",9218:"6cdc45fa",9267:"c2002008",9281:"e9be8bce",9293:"76b07081",9337:"40b94b8f",9383:"2197bb5a",9408:"9f41b422",9410:"b062161c",9418:"92bb0b8d",9449:"5649b27f",9453:"64e7e943",9456:"b3fe6c37",9501:"e7848886",9505:"feef6f86",9534:"73f274a6",9558:"1ea70e8c",9576:"1eb4c6cd",9583:"f55afc9c",9616:"4204c3a2",9627:"e81300bc",9655:"0ab8c684",9680:"f8810478",9684:"942d7bd8",9686:"13e22469",9690:"47ad6244",9789:"f53819a7",9827:"1e4ec293",9834:"a67bbe02",9836:"65979fe6",9862:"4e4e15e1",9868:"09ab30ae",9985:"0b5de004"}[e]+".chunk.js",c.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),c.o=(e,t)=>Object.prototype.hasOwnProperty.call(e,t),n={},a="lite:",c.l=(e,t,o,i)=>{if(n[e])n[e].push(t);else{var r,g;if(void 0!==o)for(var d=document.getElementsByTagName("script"),b=0;b<d.length;b++){var f=d[b];if(f.getAttribute("src")==e||f.getAttribute("data-webpack")==a+o){r=f;break}}r||(g=!0,(r=document.createElement("script")).charset="utf-8",r.timeout=120,c.nc&&r.setAttribute("nonce",c.nc),r.setAttribute("data-webpack",a+o),r.src=e),n[e]=[t];var l=(t,a)=>{r.onerror=r.onload=null,clearTimeout(C);var o=n[e];if(delete n[e],r.parentNode&&r.parentNode.removeChild(r),o&&o.forEach((e=>e(a))),t)return t(a)},C=setTimeout(l.bind(null,void 0,{type:"timeout",target:r}),12e4);r.onerror=l.bind(null,r.onerror),r.onload=l.bind(null,r.onload),g&&document.head.appendChild(r)}},c.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},c.nmd=e=>(e.paths=[],e.children||(e.children=[]),e),c.p="https://cdn-client.medium.com/lite/",(()=>{var e={6700:0},t=[];c.f.j=(t,n)=>{var a=c.o(e,t)?e[t]:void 0;if(0!==a)if(a)n.push(a[2]);else{var o=new Promise(((n,o)=>{a=e[t]=[n,o]}));n.push(a[2]=o);var i=c.p+c.u(t),r=new Error;c.l(i,(n=>{if(c.o(e,t)&&(0!==(a=e[t])&&(e[t]=void 0),a)){var o=n&&("load"===n.type?"missing":n.type),i=n&&n.target&&n.target.src;r.message="Loading chunk "+t+" failed.\n("+o+": "+i+")",r.name="ChunkLoadError",r.type=o,r.request=i,a[1](r)}}),"chunk-"+t,t)}};var n=e=>{},a=(a,o)=>{for(var i,r,[g,d,b,f]=o,l=0,C=[];l<g.length;l++)r=g[l],c.o(e,r)&&e[r]&&C.push(e[r][0]),e[r]=0;for(i in d)c.o(d,i)&&(c.m[i]=d[i]);for(b&&b(c),a&&a(o);C.length;)C.shift()();return f&&t.push.apply(t,f),n()},o=self.webpackChunklite=self.webpackChunklite||[];function i(){for(var n,a=0;a<t.length;a++){for(var o=t[a],i=!0,r=1;r<o.length;r++){var g=o[r];0!==e[g]&&(i=!1)}i&&(t.splice(a--,1),n=c(c.s=o[0]))}return 0===t.length&&(c.x(),c.x=e=>{}),n}o.forEach(a.bind(null,0)),o.push=a.bind(null,o.push.bind(o));var r=c.x;c.x=()=>(c.x=r||(e=>{}),(n=i)())})(),c.x()})();
//# sourceMappingURL=https://stats.medium.build/lite/sourcemaps/manifest.d192dac9.js.map