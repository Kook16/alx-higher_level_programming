(self.webpackChunklite=self.webpackChunklite||[]).push([[8491],{18978:(e,t,n)=>{"use strict";n.d(t,{L:()=>d});var o=n(67294),l=n(71652),i=n(82405),r=n(77355),c=n(20113),a=n(87691),s=n(21372),d=function(e){var t=e.collection,n=e.buttonSize,d=e.buttonStyleFn,u=t.name,p=t.description;return o.createElement(r.x,{padding:"15px",display:"flex",flexDirection:"column",width:"300px"},o.createElement(r.x,{display:"flex",flexDirection:"row",justifyContent:"space-between",whiteSpace:"normal",borderBottom:"neutral.primary",paddingBottom:"10px",marginBottom:"10px"},o.createElement(r.x,{display:"flex",flexDirection:"column",paddingRight:"5px"},o.createElement(c.X6,{scale:"S"},u),o.createElement(a.F,{scale:"S"},p)),o.createElement(r.x,null,o.createElement(l.v,{collection:t,link:!0}))),o.createElement(r.x,{display:"flex",flexDirection:"row",alignItems:"center",justifyContent:"space-between"},o.createElement(a.F,{scale:"M"},"Followed by ",(0,s.pY)(t.subscriberCount||0)," people"),o.createElement(i.F,{collection:t,buttonSize:n,buttonStyleFn:d,susiEntry:"follow_card"})))}},21309:(e,t,n)=>{"use strict";n.d(t,{t:()=>c});var o=n(67294),l=n(77355),i=n(14646),r=function(e){var t;return{fontWeight:null!==(t=e.newFonts.detail.boldWeight)&&void 0!==t?t:"bold"}},c=function(e){var t=e.collection,n=e.marginLeft,c=(0,i.I)();return t?o.createElement(l.x,{marginLeft:n,display:"inline-block"},o.createElement("strong",{className:c(r)},t.name)):null}},82405:(e,t,n)=>{"use strict";n.d(t,{F:()=>h});var o=n(34699),l=n(21919),i=n(67294),r=n(51615),c=n(77520),a=n(20297),s=n(25550),d=n(25267),u=n(39727),p=n(26350),m=n(50563),f=n(93310),v=n(77355),b=n(47230),g=n(18627),w=n(66411),E=n(92661),C=n(43487),y=n(50458),h=function(e){var t,n=e.buttonSize,y=e.buttonStyleFn,h=e.collection,x=e.post,P=e.simpleLink,S=e.susiEntry,k=void 0===S?"follow_card":S,F=e.preventParentClick,D=e.width,I=(0,C.v9)((function(e){return e.config.authDomain})),T=(0,s.r)().viewerId,R=(0,g.A)(),j=(0,w.pK)(),A=(0,r.TH)(),L=(0,E.$B)(A.pathname),N=null==L||null===(t=L.route)||void 0===t?void 0:t.name,_=(0,u.g)(h),U=_.viewerEdge,B=_.loading,z=function(e,t){var n=(0,l.D)(a.e),r=(0,o.Z)(n,1)[0];return i.useCallback((function(){return r({variables:{id:e.id},optimisticResponse:{followCollection:{__typename:"Collection",id:e.id,name:e.name,viewerEdge:{__typename:"CollectionViewerEdge",id:"collectionId:".concat(e.id,"-viewerId:").concat(t),isFollowing:!0}}},update:function(n){n.modify({id:"User:".concat(t),fields:{missionControl:(0,m.im)("followedCollections",!0),followingCollectionConnection:(0,m.Hc)(e.id)}})}})}),[e.id])}(h,T),K=function(e,t){var n=(0,l.D)(a.X),r=(0,o.Z)(n,1)[0];return i.useCallback((function(){return r({variables:{id:e.id},optimisticResponse:{unfollowCollection:{__typename:"Collection",id:e.id,name:e.name,viewerEdge:{__typename:"CollectionViewerEdge",id:"collectionId:".concat(e.id,"-viewerId:").concat(t),isFollowing:!1}}},update:function(e){e.modify({id:"User:".concat(t),fields:{missionControl:(0,m.im)("followedCollections",!1)}})}})}),[e.id])}(h,T),M=i.useCallback((function(e){F&&e.preventDefault(),R.event("collection.followed",{collectionId:h.id,followSource:j}),z()}),[h,F,j,R]),H=i.useCallback((function(e){F&&e.preventDefault(),R.event("collection.unfollowed",{collectionId:h.id,followSource:j}),K()}),[F,j,R]),G=!(null==U||!U.isFollowing),V=y?y(!!G):G?"OBVIOUS":"STRONG";return P?i.createElement(f.r,{onClick:G?H:M},i.createElement(v.x,{display:"flex",flexDirection:"row"},G?"Unfollow publication":"Follow publication")):i.createElement(d.I,null,(function(e){return e?i.createElement(b.zx,{size:n,onClick:G?H:M,buttonStyle:V,loading:B,width:D},G?"Following":"Follow"):i.createElement(p.R,{collection:h,buttonStyle:V,isButton:!0,buttonSize:n,operation:"register",actionUrl:O(I,h,x)||"",susiEntry:k,pageSource:(0,c.x)(N,"register"),buttonWidth:D},G?"Following":"Follow")}))},O=function(e,t,n){return t.slug&&(n&&n.id?(0,y.TA)(e,t.slug,n.id):(0,y.Ll)(e,t.slug))}},26700:(e,t,n)=>{"use strict";n.d(t,{q:()=>d});var o=n(67294),l=n(18978),i=n(68427),r=n(69992),c=n(93310),a=n(30020),s=n(87691),d=function(e){var t=e.collection,n=e.clamp,d=e.popoverPlacement,u=void 0===d?"bottom":d,p=e.scale,m=void 0===p?"M":p,f=e.testId,v=(0,i.R)(t);return o.createElement(r.$,{placement:u,targetDistance:10,mouseLeaveDelay:100,mouseEnterDelay:a.w,popoverRenderFn:function(){return o.createElement(l.L,{collection:t})},display:"block"},o.createElement(c.r,{inline:!0,href:v,linkStyle:"SUBTLE",display:"flex",rules:{alignItems:"center"},"data-testid":f},o.createElement(s.F,{scale:m,color:"DARKER",clamp:n},t.name)))}},34796:(e,t,n)=>{"use strict";n.d(t,{F:()=>a});var o,l=n(67294),i=n(21309),r=n(6443),c=n(39727);!function(e){e.CollectionPendingAsEditorAndAuthor="CollectionPendingAsEditorAndAuthor",e.CollectionPendingKnown="CollectionPendingKnown",e.CollectionPending="CollectionPending",e.CollectionUnsubmitted="CollectionUnsubmitted",e.Normal="Normal"}(o||(o={}));var a=function(e){var t=e.post,n=s(t);if(!t||!n)return null;var r=t.pendingCollection,c=l.createElement(i.t,{collection:r,marginLeft:"4px"});switch(n){case o.CollectionPendingAsEditorAndAuthor:return l.createElement(l.Fragment,null,"Draft in",c);case o.CollectionPendingKnown:return l.createElement(l.Fragment,null,"Draft submitted to",c);case o.CollectionPending:return l.createElement(l.Fragment,null,"Submitted draft");case o.CollectionUnsubmitted:return l.createElement(l.Fragment,null,"Unsubmitted draft");case o.Normal:return l.createElement(l.Fragment,null,"Draft")}},s=function(e){var t,n=(0,r.H)().value,l=null==e?void 0:e.pendingCollection,i=null==e||null===(t=e.creator)||void 0===t?void 0:t.id,a=!!n&&!(null==l||!l.creator)&&l.creator.id===n.id,s=(0,c.g)(l).viewerEdge,d=null==s?void 0:s.isEditor,u=a||d,p=u||!!n&&n.id===i,m=p&&l;return!e||e.isPublished?null:p&&"PENDING"===e.statusForCollection?m?u&&n&&n.id===i?o.CollectionPendingAsEditorAndAuthor:o.CollectionPendingKnown:o.CollectionPending:"NOT_YET_SUBMITTED"===e.statusForCollection?o.CollectionUnsubmitted:o.Normal}},9272:(e,t,n)=>{"use strict";n.d(t,{n:()=>x});var o=n(96156),l=n(67294),i=n(93310),r=n(30020),c=n(87691),a=n(18627),s=n(66411),d=n(14646);function u(){return u=Object.assign?Object.assign.bind():function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var o in n)Object.prototype.hasOwnProperty.call(n,o)&&(e[o]=n[o])}return e},u.apply(this,arguments)}var p=l.createElement("path",{d:"M18 16.8a7.14 7.14 0 0 0 2.24-5.32c0-4.12-3.53-7.48-8.05-7.48C7.67 4 4 7.36 4 11.48c0 4.13 3.67 7.48 8.2 7.48a8.9 8.9 0 0 0 2.38-.32c.23.2.48.39.75.56 1.06.69 2.2 1.04 3.4 1.04.22 0 .4-.11.48-.29a.5.5 0 0 0-.04-.52 6.4 6.4 0 0 1-1.16-2.65v.02zm-3.12 1.06l-.06-.22-.32.1a8 8 0 0 1-2.3.33c-4.03 0-7.3-2.96-7.3-6.59S8.17 4.9 12.2 4.9c4 0 7.1 2.96 7.1 6.6 0 1.8-.6 3.47-2.02 4.72l-.2.16v.26l.02.3a6.74 6.74 0 0 0 .88 2.4 5.27 5.27 0 0 1-2.17-.86c-.28-.17-.72-.38-.94-.59l.01-.02z"});const m=function(e){return l.createElement("svg",u({width:24,height:24,viewBox:"0 0 24 24"},e),p)};function f(){return f=Object.assign?Object.assign.bind():function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var o in n)Object.prototype.hasOwnProperty.call(n,o)&&(e[o]=n[o])}return e},f.apply(this,arguments)}var v=l.createElement("path",{fillRule:"evenodd",clipRule:"evenodd",d:"M18.47 20.27a6.08 6.08 0 0 1-4.06-1.55c-.74.2-1.51.3-2.29.3-4.48 0-8.12-3.35-8.12-7.48 0-4.15 3.64-7.5 8.12-7.5 4.48 0 8.12 3.35 8.12 7.48 0 1.98-.81 3.83-2.3 5.23.02.17.05.34.1.53.2.66.52 1.33 1 1.96a.66.66 0 0 1-.53 1.04h-.04z"});const b=function(e){return l.createElement("svg",f({width:24,height:24,viewBox:"0 0 24 24"},e),v)};function g(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);t&&(o=o.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,o)}return n}function w(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?g(Object(n),!0).forEach((function(t){(0,o.Z)(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):g(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}var E=function(e,t){return"LIGHTER"===t?e.colorTokens.foreground.neutral.primary.hover:e.colorTokens.foreground.neutral.secondary.base},C=function(e,t){return function(n){return{cursor:t?"not-allowed":"pointer",border:0,opacity:1,padding:"4px 0",display:"flex",alignItems:"center",fill:"LIGHTER"===e?n.colorTokens.foreground.neutral.secondary.base:n.baseColor.fill.light,":hover":t?void 0:{fill:E(n,e),"& p":{color:E(n,e)}}}}},y=function(e){return{cursor:"not-allowed",fill:e.colorTokens.foreground.neutral.secondary.base,opacity:.25}},h=function(e){var t=e.disabled,n=e.handleClick,o=e.href,r=e.children,c=e.responsesCountColor,a=e.testId,s=(0,d.I)();return o?l.createElement(i.r,{onClick:n,href:o,rules:C(c,t),"aria-label":"responses",disabled:t,"data-testid":a},r):l.createElement("button",{onClick:n,className:s(C(c,t)),"aria-label":"responses",disabled:t,"data-testid":a},r)},O=function(e){var t=e.disabled,n=e.iconStylesOverride,o=(0,d.I)();return t?l.createElement(b,{className:o([y])}):l.createElement(m,{className:o([n])})},x=function(e){var t=e.disabled,n=e.disabledTooltipText,o=void 0===n?"":n,i=e.responsesCount,u=e.handleClick,p=e.trackingData,m=e.iconStylesOverride,f=e.countStylesOverride,v=e.responsesCountColor,b=void 0===v?"LIGHTER":v,g=e.responsesCountScale,E=void 0===g?"M":g,C=e.href,y=(0,d.I)(),x=(0,a.A)(),P=(0,s.pK)(),S=!t&&i,k=(0,l.useCallback)((function(e){null==u||u(e),x.event("responses.viewAllClicked",w(w({},p),{},{source:P}))}),[x,u,p,P]);return l.createElement(r._,{tooltipText:t?o:"Respond",targetDistance:15},l.createElement(h,{handleClick:t?void 0:k,responsesCountColor:b,disabled:t,href:C},l.createElement(O,{disabled:t,iconStylesOverride:m}),!!S&&l.createElement(c.F,{scale:E,color:b},l.createElement("span",{className:"pw-responses-count ".concat(y([f]))},i))))}},38160:(e,t,n)=>{"use strict";n.d(t,{c:()=>r});var o=n(22122),l=n(67294),i=n(9272),r=function(e){var t=!e.allowResponses||e.isLimitedState||!e.isPublished,n=(0,l.useMemo)((function(){return e.isPublished?e.allowResponses?e.isLimitedState?"This feature is temporarily disabled":void 0:"Responses hidden":"You cannot respond to a draft"}),[e.isPublished,e.allowResponses,e.isLimitedState]);return l.createElement(i.n,(0,o.Z)({},e,{disabled:t,disabledTooltipText:n}))}},58992:(e,t,n)=>{"use strict";n.d(t,{l:()=>o});var o=function(e){return"APPROVED"===e.statusForCollection&&e.isPublished}}}]);
//# sourceMappingURL=https://stats.medium.build/lite/sourcemaps/8491.7fa46461.chunk.js.map