"use strict";(self.webpackChunkfis_scraper_frontend=self.webpackChunkfis_scraper_frontend||[]).push([[765],{8765:(Me,U,i)=>{i.r(U),i.d(U,{ScraperModule:()=>we});var c=i(6895),x=i(7024),N=i(1702),o=i(4006),S=i(7337),e=i(4650),d=i(3546),A=i(3848),m=i(7340),J=i(7579),y=i(2722),F=i(1831);const E=(0,F.ZF)("races");var D=i(9765),R=i(2184),_=i(7392),q=i(1481),g=i(3014),p=i(4859),w=i(4850),h=i(6338),f=i(3162),O=i(266),L=i(1572);let M=(()=>{class t{constructor(){}}return t.\u0275fac=function(r){return new(r||t)},t.\u0275cmp=e.Xpm({type:t,selectors:[["app-file-spinner"]],decls:1,vars:0,consts:[["mode","indeterminate","diameter","30","color","accent"]],template:function(r,n){1&r&&e._UZ(0,"mat-spinner",0)},dependencies:[L.Ou],styles:["[_nghost-%COMP%]{align-items:center;display:flex;height:2rem;justify-content:center;width:100%}"],changeDetection:0}),t})();function Y(t,a){if(1&t){const r=e.EpF();e.TgZ(0,"mat-card-actions",6)(1,"button",7),e.NdJ("click",function(){e.CHM(r),e.oxw();const s=e.MAs(11),I=e.oxw();return e.KtG(I.downloadAll(s.selectedOptions.selected))}),e._uU(2),e.TgZ(3,"mat-icon"),e._uU(4," download"),e.qZA()()()}if(2&t){const r=e.oxw().ngIf,n=e.MAs(11);e.xp6(2),e.hij(" ",r.length>n.selectedOptions.selected.length?"DOWNLOAD SELECTED":"DOWNLOAD ALL"," ")}}function Q(t,a){if(1&t&&e._UZ(0,"mat-progress-bar",8),2&t){const r=a.ngIf;e.Q6J("mode","PENDING"===r.state?"buffer":"determinate")("value",r.progress)("color","DONE"===r.state||"IN_PROGRES"===r.state?"accent":"warn")}}function k(t,a){if(1&t){const r=e.EpF();e.ynx(0),e.TgZ(1,"mat-list-option",9),e._UZ(2,"mat-icon",10),e.TgZ(3,"div",11),e._uU(4),e.qZA(),e.TgZ(5,"div",12),e._uU(6),e.ALo(7,"date"),e.qZA()(),e.TgZ(8,"button",13),e.NdJ("click",function(s){const Oe=e.CHM(r).$implicit,Le=e.oxw(2);return e.KtG(Le.downloadFile(s,Oe))}),e.TgZ(9,"mat-icon"),e._uU(10," download"),e.qZA()(),e.BQk()}if(2&t){const r=a.$implicit;e.xp6(1),e.Q6J("value",r.uuid)("@currentFileEnter",void 0),e.xp6(1),e.Q6J("svgIcon","team"!==r.kind||r.details?"csv_file":"zip_file"),e.xp6(2),e.AsE("",r.place," ",r.hill_size,""),e.xp6(2),e.Oqu(e.xi3(7,7,r.date,"medium")),e.xp6(2),e.Q6J("matTooltip","Download "+r.place+" "+r.hill_size)}}function P(t,a){1&t&&e._UZ(0,"app-file-spinner")}function B(t,a){if(1&t&&(e.ynx(0),e.TgZ(1,"mat-card")(2,"mat-card-header",1)(3,"mat-card-title"),e._uU(4,"Current files:"),e.qZA(),e.YNc(5,Y,5,1,"mat-card-actions",2),e.YNc(6,Q,1,3,"mat-progress-bar",3),e.ALo(7,"async"),e.qZA(),e._UZ(8,"mat-divider"),e.TgZ(9,"mat-card-content")(10,"mat-selection-list",null,4),e.YNc(12,k,11,10,"ng-container",5),e.qZA(),e.YNc(13,P,1,0,"app-file-spinner",0),e.ALo(14,"async"),e.qZA()(),e.BQk()),2&t){const r=a.ngIf,n=e.oxw();e.xp6(5),e.Q6J("ngIf",r.length>1),e.xp6(1),e.Q6J("ngIf",e.lcZ(7,5,n.download$)),e.xp6(6),e.Q6J("ngForOf",r)("ngForTrackBy",n.trackByUuid),e.xp6(1),e.Q6J("ngIf",e.lcZ(14,7,n.spinnerState$))}}let $=(()=>{class t{constructor(r,n,s,I){this.iconRegistry=r,this.sanitizer=n,this.scraperService=s,this.store=I,this.destroySubject$=new J.x,this.destroy$=this.destroySubject$.asObservable(),this.trackByUuid=R.k,r.addSvgIcon("csv_file",n.bypassSecurityTrustResourceUrl("assets/csv.svg")),r.addSvgIcon("zip_file",n.bypassSecurityTrustResourceUrl("assets/zip.svg"))}ngOnInit(){this.files$=this.store.select(E),this.spinnerState$=this.store.select(D.M)}downloadAll(r){const n=r.map(s=>s.value);this.scraperService.downloadSelectedFiles(n).pipe((0,y.R)(this.destroy$)).subscribe()}downloadFile(r,n){r.stopImmediatePropagation(),r.stopPropagation(),r.preventDefault(),this.scraperService.downloadFile(n).pipe((0,y.R)(this.destroy$)).subscribe()}ngOnDestroy(){this.destroySubject$.next(null)}}return t.\u0275fac=function(r){return new(r||t)(e.Y36(_.jv),e.Y36(q.H7),e.Y36(g.V),e.Y36(F.yh))},t.\u0275cmp=e.Xpm({type:t,selectors:[["app-current-files"]],decls:2,vars:3,consts:[[4,"ngIf"],[1,"header"],["align","end",4,"ngIf"],[3,"mode","value","color",4,"ngIf"],["races",""],[4,"ngFor","ngForOf","ngForTrackBy"],["align","end"],["mat-button","","matTooltip","Download all files as .zip",3,"click"],[3,"mode","value","color"],["selected","true",1,"mat-elevation-z1","expanded",3,"value"],["matListItemIcon","",3,"svgIcon"],["matListItemTitle",""],["matListItemLine",""],["mat-icon-button","",3,"matTooltip","click"]],template:function(r,n){1&r&&(e.YNc(0,B,15,9,"ng-container",0),e.ALo(1,"async")),2&r&&e.Q6J("ngIf",e.lcZ(1,1,n.files$))},dependencies:[p.lW,p.RK,d.a8,d.hq,d.dn,d.dk,d.n5,w.d,_.Hw,h.Ub,h.vS,h.Yt,h.WW,h.sL,f.pW,O.gM,c.sg,c.O5,M,c.Ov,c.uU],styles:["mat-card[_ngcontent-%COMP%]{width:min(70rem,100%);min-height:15rem;margin:2rem auto}mat-card-header[_ngcontent-%COMP%]{display:flex}mat-card-title[_ngcontent-%COMP%]{display:inline-block}mat-card-actions[_ngcontent-%COMP%]{display:inline-block;margin-left:auto;margin-bottom:0}mat-selection-list[_ngcontent-%COMP%]{display:flex;flex-flow:row wrap}mat-list-option[_ngcontent-%COMP%]{width:calc(100% - 5rem)}button[_ngcontent-%COMP%]{margin:auto}"],data:{animation:[(0,m.X$)("currentFileEnter",[(0,m.eR)(":enter",[(0,m.oB)({width:"0px",minWidth:"0"}),(0,m.jt)("500ms cubic-bezier(0.4, 0.0, 0.2, 1)",(0,m.oB)({width:"*"}))])])]},changeDetection:0}),t})();var Z=i(4144),l=i(9549),b=i(455);let T=(()=>{class t{transform(r,n){return r.hasError(n)}}return t.\u0275fac=function(r){return new(r||t)},t.\u0275pipe=e.Yjl({name:"hasError",type:t,pure:!0}),t})();function G(t,a){1&t&&(e.TgZ(0,"mat-error"),e._uU(1," Enter "),e.TgZ(2,"strong"),e._uU(3,"number"),e.qZA(),e._uU(4," greater than 0 "),e.qZA())}function W(t,a){1&t&&(e.TgZ(0,"mat-error"),e._uU(1," Enter "),e.TgZ(2,"strong"),e._uU(3,"number"),e.qZA()())}function z(t,a){1&t&&(e.TgZ(0,"mat-error"),e._uU(1," FIS ID is "),e.TgZ(2,"strong"),e._uU(3,"required"),e.qZA()())}function j(t,a){if(1&t&&(e.TgZ(0,"div",8)(1,"mat-form-field",9)(2,"mat-label"),e._uU(3,"FIS ID"),e.qZA(),e._UZ(4,"input",10),e.YNc(5,G,5,0,"mat-error",11),e.ALo(6,"hasError"),e.YNc(7,W,4,0,"mat-error",11),e.ALo(8,"hasError"),e.YNc(9,z,4,0,"mat-error",11),e.ALo(10,"hasError"),e.qZA(),e.TgZ(11,"mat-slide-toggle",12),e._uU(12,"Details"),e.qZA()()),2&t){const r=a.index,n=a.first,s=e.oxw();e.Q6J("formGroupName",r)("@changeInputsNumber",!n),e.xp6(5),e.Q6J("ngIf",e.xi3(6,5,s.fisId[r],"min")),e.xp6(2),e.Q6J("ngIf",e.xi3(8,8,s.fisId[r],"pattern")),e.xp6(2),e.Q6J("ngIf",e.xi3(10,11,s.fisId[r],"required"))}}function X(t,a){1&t&&e._UZ(0,"mat-progress-bar",13),2&t&&e.Q6J("value",a.ngIf)}const H=[(0,m.oB)({height:"0"}),(0,m.jt)("500ms cubic-bezier(0.4, 0.0, 0.2, 1)",(0,m.oB)({height:"*"}))],V=[(0,m.oB)({height:"*"}),(0,m.jt)("500ms cubic-bezier(0.4, 0.0, 0.2, 1)",(0,m.oB)({height:"0"}))];let K=(()=>{class t{constructor(r,n){this.formBuilder=r,this.scraperService=n,this.fisId=[],this.details=new o.NI(!1),this.trackByIndex=R.z,this.raceForm=this.formBuilder.group({races:this.formBuilder.array([this.newRace()])}),this.races=this.raceForm.get("races")}newRace(){return this.fisId.push(new o.NI(0,[o.kI.required,o.kI.min(1),o.kI.pattern(/\d*/)])),this.formBuilder.group({fis_id:this.fisId[this.fisId.length-1],details:this.details})}addInput(){this.races.push(this.newRace())}removeInput(){this.fisId.pop(),this.races.removeAt(this.races.length-1)}submit(){this.raceForm.valid&&(this.progress$=this.scraperService.scrapMultipleRaces(this.raceForm.value.races))}}return t.\u0275fac=function(r){return new(r||t)(e.Y36(o.qu),e.Y36(g.V))},t.\u0275cmp=e.Xpm({type:t,selectors:[["app-multi-races"]],decls:16,vars:7,consts:[[3,"formGroup"],["formArrayName","races",1,"multi-races-form"],["class","multi-races-form-group",3,"formGroupName",4,"ngFor","ngForOf","ngForTrackBy"],[1,"multi-races-form-controls"],["mat-icon-button","","color","accent",3,"click"],["mat-icon-button","","color","warn",3,"click"],["mat-raised-button","","color","primary",1,"multi-races-form-submit",3,"disabled","click"],["color","accent","mode","buffer",3,"value",4,"ngIf"],[1,"multi-races-form-group",3,"formGroupName"],["appearance","outline"],["matInput","","type","number","formControlName","fis_id"],[4,"ngIf"],["formControlName","details"],["color","accent","mode","buffer",3,"value"]],template:function(r,n){1&r&&(e.TgZ(0,"form",0)(1,"div",1)(2,"h2"),e._uU(3,"Scrap multiple races"),e.qZA(),e.YNc(4,j,13,14,"div",2),e.TgZ(5,"div",3)(6,"button",4),e.NdJ("click",function(){return n.addInput()}),e.TgZ(7,"mat-icon"),e._uU(8,"exposure_plus_1"),e.qZA()(),e.TgZ(9,"button",5),e.NdJ("click",function(){return n.removeInput()}),e.TgZ(10,"mat-icon"),e._uU(11,"exposure_neg_1"),e.qZA()()(),e.TgZ(12,"button",6),e.NdJ("click",function(){return n.submit()}),e._uU(13," Scrap! "),e.qZA()()(),e.YNc(14,X,1,1,"mat-progress-bar",7),e.ALo(15,"async")),2&r&&(e.Q6J("formGroup",n.raceForm),e.xp6(4),e.Q6J("ngForOf",n.races.controls)("ngForTrackBy",n.trackByIndex),e.xp6(8),e.Q6J("disabled",!n.raceForm.valid),e.xp6(2),e.Q6J("ngIf",e.lcZ(15,5,n.progress$)))},dependencies:[p.lW,p.RK,_.Hw,Z.Nt,l.KE,l.hX,l.TO,f.pW,b.Rr,c.sg,c.O5,o._Y,o.Fj,o.wV,o.JJ,o.JL,o.sg,o.u,o.x0,o.CE,c.Ov,T],styles:[".multi-races-form[_ngcontent-%COMP%]{width:min(40rem,100%);padding:3rem;display:flex;flex-direction:column}.multi-races-form-controls[_ngcontent-%COMP%]{display:flex;justify-content:flex-end;gap:.5rem}.multi-races-form-group[_ngcontent-%COMP%]{overflow:hidden;display:flex;gap:.5rem;flex-direction:column}.multi-races-form-group[_ngcontent-%COMP%] + .multi-races-form-group[_ngcontent-%COMP%]{margin-block:.5rem}.multi-races-form-submit[_ngcontent-%COMP%]{margin-top:3rem}mat-suffix[_ngcontent-%COMP%]{max-height:2rem}mat-form-field[_ngcontent-%COMP%]{margin-top:1rem}"],data:{animation:[(0,m.X$)("changeInputsNumber",[(0,m.eR)(":enter",H),(0,m.eR)(":leave",V)])]},changeDetection:0}),t})();function ee(t,a){1&t&&(e.TgZ(0,"mat-error"),e._uU(1," Enter "),e.TgZ(2,"strong"),e._uU(3,"number"),e.qZA(),e._uU(4," greater than 0 "),e.qZA())}function te(t,a){1&t&&(e.TgZ(0,"mat-error"),e._uU(1," Enter "),e.TgZ(2,"strong"),e._uU(3,"number"),e.qZA()())}function re(t,a){1&t&&(e.TgZ(0,"mat-error"),e._uU(1," Initial FIS ID is "),e.TgZ(2,"strong"),e._uU(3,"required"),e.qZA()())}function ne(t,a){1&t&&(e.TgZ(0,"mat-error"),e._uU(1," Enter "),e.TgZ(2,"strong"),e._uU(3,"number"),e.qZA(),e._uU(4," greater than 0 "),e.qZA())}function ae(t,a){1&t&&(e.TgZ(0,"mat-error"),e._uU(1," Enter "),e.TgZ(2,"strong"),e._uU(3,"number"),e.qZA()())}function oe(t,a){1&t&&(e.TgZ(0,"mat-error"),e._uU(1," Final FIS ID is "),e.TgZ(2,"strong"),e._uU(3,"required"),e.qZA()())}function ie(t,a){1&t&&e._UZ(0,"mat-progress-bar",8),2&t&&e.Q6J("value",a.ngIf)}let se=(()=>{class t{constructor(r,n){this.formBuilder=r,this.scraperService=n,this.startFisId=new o.NI(0,[o.kI.required,o.kI.min(1),o.kI.pattern(/\d*/)]),this.endFisId=new o.NI(0,[o.kI.required,o.kI.min(1),o.kI.pattern(/\d*/)]),this.details=new o.NI(!1),this.raceForm=this.formBuilder.group({start_fis_id:this.startFisId,end_fis_id:this.endFisId,details:this.details})}submit(){this.raceForm.valid&&(this.progress$=this.scraperService.scrapRangeOfRaces(this.raceForm.value))}}return t.\u0275fac=function(r){return new(r||t)(e.Y36(o.qu),e.Y36(g.V))},t.\u0275cmp=e.Xpm({type:t,selectors:[["app-range-races"]],decls:29,vars:29,consts:[[1,"range-races-form",3,"formGroup"],["appearance","outline"],["matInput","","type","number","formControlName","start_fis_id"],[4,"ngIf"],["matInput","","type","number","formControlName","end_fis_id"],["formControlName","details"],["mat-raised-button","","color","primary",1,"range-races-form-submit",3,"disabled","click"],["color","accent","mode","buffer",3,"value",4,"ngIf"],["color","accent","mode","buffer",3,"value"]],template:function(r,n){1&r&&(e.TgZ(0,"form",0)(1,"h2"),e._uU(2,"Scrap races in range of IDs"),e.qZA(),e.TgZ(3,"mat-form-field",1)(4,"mat-label"),e._uU(5,"Initial FIS ID"),e.qZA(),e._UZ(6,"input",2),e.YNc(7,ee,5,0,"mat-error",3),e.ALo(8,"hasError"),e.YNc(9,te,4,0,"mat-error",3),e.ALo(10,"hasError"),e.YNc(11,re,4,0,"mat-error",3),e.ALo(12,"hasError"),e.qZA(),e.TgZ(13,"mat-form-field",1)(14,"mat-label"),e._uU(15,"Final FIS ID"),e.qZA(),e._UZ(16,"input",4),e.YNc(17,ne,5,0,"mat-error",3),e.ALo(18,"hasError"),e.YNc(19,ae,4,0,"mat-error",3),e.ALo(20,"hasError"),e.YNc(21,oe,4,0,"mat-error",3),e.ALo(22,"hasError"),e.qZA(),e.TgZ(23,"mat-slide-toggle",5),e._uU(24,"Details"),e.qZA(),e.TgZ(25,"button",6),e.NdJ("click",function(){return n.submit()}),e._uU(26," Scrap! "),e.qZA()(),e.YNc(27,ie,1,1,"mat-progress-bar",7),e.ALo(28,"async")),2&r&&(e.Q6J("formGroup",n.raceForm),e.xp6(7),e.Q6J("ngIf",e.xi3(8,9,n.startFisId,"min")),e.xp6(2),e.Q6J("ngIf",e.xi3(10,12,n.startFisId,"pattern")),e.xp6(2),e.Q6J("ngIf",e.xi3(12,15,n.startFisId,"required")),e.xp6(6),e.Q6J("ngIf",e.xi3(18,18,n.endFisId,"min")),e.xp6(2),e.Q6J("ngIf",e.xi3(20,21,n.endFisId,"pattern")),e.xp6(2),e.Q6J("ngIf",e.xi3(22,24,n.endFisId,"required")),e.xp6(4),e.Q6J("disabled",!n.raceForm.valid),e.xp6(2),e.Q6J("ngIf",e.lcZ(28,27,n.progress$)))},dependencies:[p.lW,Z.Nt,l.KE,l.hX,l.TO,f.pW,b.Rr,c.O5,o._Y,o.Fj,o.wV,o.JJ,o.JL,o.sg,o.u,c.Ov,T],styles:[".range-races-form[_ngcontent-%COMP%]{width:min(40rem,100%);padding:3rem;display:flex;gap:.5rem;flex-direction:column}.range-races-form-submit[_ngcontent-%COMP%]{margin-top:3rem}"],changeDetection:0}),t})();var v=i(9646),u=i(7274);let ce=(()=>{class t{}return t.\u0275fac=function(r){return new(r||t)},t.\u0275cmp=e.Xpm({type:t,selectors:[["app-scrap-table-dialog"]],decls:10,vars:0,consts:[["mat-dialog-title",""],[1,"mat-typography"],["align","end"],["mat-button","","mat-dialog-close",""]],template:function(r,n){1&r&&(e.TgZ(0,"h2",0),e._uU(1,"Scrap table"),e.qZA(),e.TgZ(2,"mat-dialog-content",1)(3,"p"),e._uU(4," Scraps data from all tables at given URL. Please make sure that that data is really displayed in HTML table tags. "),e.qZA(),e.TgZ(5,"p"),e._uU(6," Doesn't work with fis-ski.com;) It looks like a table but it's not a table from HTML point of view. "),e.qZA()(),e.TgZ(7,"mat-dialog-actions",2)(8,"button",3),e._uU(9,"Close"),e.qZA()())},dependencies:[p.lW,u.ZT,u.uh,u.xY,u.H8],encapsulation:2,changeDetection:0}),t})();function le(t,a){1&t&&(e.TgZ(0,"mat-error"),e._uU(1," URL is "),e.TgZ(2,"strong"),e._uU(3,"required"),e.qZA()())}function me(t,a){1&t&&(e.TgZ(0,"mat-error"),e._uU(1," Enter "),e.TgZ(2,"strong"),e._uU(3,"valid"),e.qZA(),e._uU(4," URL "),e.qZA())}function pe(t,a){1&t&&e._UZ(0,"mat-progress-bar",7),2&t&&e.Q6J("value",100*a.ngIf)}let ue=(()=>{class t{constructor(r,n,s){this.dialog=r,this.formBuilder=n,this.scraperService=s,this.url=new o.NI("",[o.kI.required]),this.details=new o.NI(!1),this.progress$=(0,v.of)(0),this.form=this.formBuilder.group({url:this.url})}submit(){this.form.valid&&(this.progress$=this.scraperService.scrapTable(this.form.value))}openDialog(){this.dialog.open(ce)}}return t.\u0275fac=function(r){return new(r||t)(e.Y36(u.uw),e.Y36(o.qu),e.Y36(g.V))},t.\u0275cmp=e.Xpm({type:t,selectors:[["app-scrap-table"]],decls:18,vars:13,consts:[[1,"single-race-form",3,"formGroup"],["mat-icon-button","",3,"click"],["appearance","outline"],["matInput","","type","url","formControlName","url"],[4,"ngIf"],["mat-raised-button","","color","primary",1,"single-race-form-submit",3,"disabled","click"],["color","accent","mode","buffer",3,"value",4,"ngIf"],["color","accent","mode","buffer",3,"value"]],template:function(r,n){1&r&&(e.TgZ(0,"form",0)(1,"h2"),e._uU(2," Scrap table "),e.TgZ(3,"button",1),e.NdJ("click",function(){return n.openDialog()}),e.TgZ(4,"mat-icon"),e._uU(5,"help"),e.qZA()()(),e.TgZ(6,"mat-form-field",2)(7,"mat-label"),e._uU(8,"URL"),e.qZA(),e._UZ(9,"input",3),e.YNc(10,le,4,0,"mat-error",4),e.ALo(11,"hasError"),e.YNc(12,me,5,0,"mat-error",4),e.ALo(13,"hasError"),e.qZA(),e.TgZ(14,"button",5),e.NdJ("click",function(){return n.submit()}),e._uU(15," Scrap! "),e.qZA()(),e.YNc(16,pe,1,1,"mat-progress-bar",6),e.ALo(17,"async")),2&r&&(e.Q6J("formGroup",n.form),e.xp6(10),e.Q6J("ngIf",e.xi3(11,5,n.url,"required")),e.xp6(2),e.Q6J("ngIf",e.xi3(13,8,n.url,"pattern")),e.xp6(2),e.Q6J("disabled",!n.form.valid),e.xp6(2),e.Q6J("ngIf",e.lcZ(17,11,n.progress$)))},dependencies:[p.lW,p.RK,_.Hw,Z.Nt,l.KE,l.hX,l.TO,f.pW,c.O5,o._Y,o.Fj,o.JJ,o.JL,o.sg,o.u,c.Ov,T],styles:[".single-race-form[_ngcontent-%COMP%]{width:min(40rem,100%);padding:3rem;display:flex;gap:.5rem;flex-direction:column}.single-race-form-submit[_ngcontent-%COMP%]{margin-top:3rem}h2[_ngcontent-%COMP%]{display:flex;align-items:center}"],changeDetection:0}),t})();function de(t,a){1&t&&(e.TgZ(0,"mat-error"),e._uU(1," Enter "),e.TgZ(2,"strong"),e._uU(3,"number"),e.qZA(),e._uU(4," greater than 0 "),e.qZA())}function ge(t,a){1&t&&(e.TgZ(0,"mat-error"),e._uU(1," Enter "),e.TgZ(2,"strong"),e._uU(3,"number"),e.qZA()())}function fe(t,a){1&t&&(e.TgZ(0,"mat-error"),e._uU(1," FIS ID is "),e.TgZ(2,"strong"),e._uU(3,"required"),e.qZA()())}function _e(t,a){1&t&&e._UZ(0,"mat-progress-bar",7),2&t&&e.Q6J("value",100*a.ngIf)}let he=(()=>{class t{constructor(r,n){this.formBuilder=r,this.scraperService=n,this.fisId=new o.NI(0,[o.kI.required,o.kI.min(1),o.kI.pattern("[0-9]*")]),this.details=new o.NI(!1),this.progress$=(0,v.of)(0),this.raceForm=this.formBuilder.group({fis_id:this.fisId,details:this.details})}submit(){this.raceForm.valid&&(this.progress$=this.scraperService.scrapRace(this.raceForm.value))}}return t.\u0275fac=function(r){return new(r||t)(e.Y36(o.qu),e.Y36(g.V))},t.\u0275cmp=e.Xpm({type:t,selectors:[["app-single-race"]],decls:19,vars:17,consts:[[1,"single-race-form",3,"formGroup"],["appearance","outline"],["matInput","","type","number","formControlName","fis_id"],[4,"ngIf"],["formControlName","details"],["mat-raised-button","","color","primary",1,"single-race-form-submit",3,"disabled","click"],["color","accent","mode","buffer",3,"value",4,"ngIf"],["color","accent","mode","buffer",3,"value"]],template:function(r,n){1&r&&(e.TgZ(0,"form",0)(1,"h2"),e._uU(2,"Scrap single race"),e.qZA(),e.TgZ(3,"mat-form-field",1)(4,"mat-label"),e._uU(5,"FIS ID"),e.qZA(),e._UZ(6,"input",2),e.YNc(7,de,5,0,"mat-error",3),e.ALo(8,"hasError"),e.YNc(9,ge,4,0,"mat-error",3),e.ALo(10,"hasError"),e.YNc(11,fe,4,0,"mat-error",3),e.ALo(12,"hasError"),e.qZA(),e.TgZ(13,"mat-slide-toggle",4),e._uU(14,"Details"),e.qZA(),e.TgZ(15,"button",5),e.NdJ("click",function(){return n.submit()}),e._uU(16," Scrap! "),e.qZA()(),e.YNc(17,_e,1,1,"mat-progress-bar",6),e.ALo(18,"async")),2&r&&(e.Q6J("formGroup",n.raceForm),e.xp6(7),e.Q6J("ngIf",e.xi3(8,6,n.fisId,"min")),e.xp6(2),e.Q6J("ngIf",e.xi3(10,9,n.fisId,"pattern")),e.xp6(2),e.Q6J("ngIf",e.xi3(12,12,n.fisId,"required")),e.xp6(4),e.Q6J("disabled",!n.raceForm.valid),e.xp6(2),e.Q6J("ngIf",e.lcZ(18,15,n.progress$)))},dependencies:[p.lW,Z.Nt,l.KE,l.hX,l.TO,f.pW,b.Rr,c.O5,o._Y,o.Fj,o.wV,o.JJ,o.JL,o.sg,o.u,c.Ov,T],styles:[".single-race-form[_ngcontent-%COMP%]{width:min(40rem,100%);padding:3rem;display:flex;gap:.5rem;flex-direction:column}.single-race-form-submit[_ngcontent-%COMP%]{margin-top:3rem}"],changeDetection:0}),t})(),Ze=(()=>{class t{}return t.\u0275fac=function(r){return new(r||t)},t.\u0275cmp=e.Xpm({type:t,selectors:[["app-raw-data-dialog"]],decls:14,vars:0,consts:[["mat-dialog-title",""],[1,"mat-typography"],["src","assets/results.png","alt","Basic results table description"],["src","assets/details.png","alt","Detailed results table description"],["align","end"],["mat-button","","mat-dialog-close",""]],template:function(r,n){1&r&&(e.TgZ(0,"h2",0),e._uU(1,"Scrap raw data"),e.qZA(),e.TgZ(2,"mat-dialog-content",1)(3,"p"),e._uU(4," This mode should be the most resistant to the errors (describing the columns is the most error prone). The downside is that data in CSV is not described. Generally it's kind of WYSIWYG mode. Data is placed in CSV in order in which it's displayed on FIS website. Please note that it means ie. that there will be no FIS code in CSV for detailed results as it's not displayed anywhere in detailed results table at fis-ski.com. "),e.qZA(),e.TgZ(5,"h3",0),e._uU(6,"Basic results table:"),e.qZA(),e._UZ(7,"img",2),e.TgZ(8,"h3",0),e._uU(9,"Detailed results table:"),e.qZA(),e._UZ(10,"img",3),e.qZA(),e.TgZ(11,"mat-dialog-actions",4)(12,"button",5),e._uU(13,"Close"),e.qZA()())},dependencies:[p.lW,u.ZT,u.uh,u.xY,u.H8],styles:["img[_ngcontent-%COMP%] {\n    width: 100%;\n  }"],changeDetection:0}),t})();function Te(t,a){1&t&&(e.TgZ(0,"mat-error"),e._uU(1," Enter "),e.TgZ(2,"strong"),e._uU(3,"number"),e.qZA(),e._uU(4," greater than 0 "),e.qZA())}function be(t,a){1&t&&(e.TgZ(0,"mat-error"),e._uU(1," Enter "),e.TgZ(2,"strong"),e._uU(3,"number"),e.qZA()())}function Ce(t,a){1&t&&(e.TgZ(0,"mat-error"),e._uU(1," FIS ID is "),e.TgZ(2,"strong"),e._uU(3,"required"),e.qZA()())}function Ie(t,a){1&t&&e._UZ(0,"mat-progress-bar",8),2&t&&e.Q6J("value",100*a.ngIf)}let Ae=(()=>{class t{constructor(r,n,s){this.dialog=r,this.formBuilder=n,this.scraperService=s,this.fisId=new o.NI(0,[o.kI.required,o.kI.min(1),o.kI.pattern("[0-9]*")]),this.details=new o.NI(!1),this.progress$=(0,v.of)(0),this.raceForm=this.formBuilder.group({fis_id:this.fisId,details:this.details})}submit(){this.raceForm.valid&&(this.progress$=this.scraperService.scrapRawData(this.raceForm.value))}openDialog(){this.dialog.open(Ze)}}return t.\u0275fac=function(r){return new(r||t)(e.Y36(u.uw),e.Y36(o.qu),e.Y36(g.V))},t.\u0275cmp=e.Xpm({type:t,selectors:[["app-unprocessed-data"]],decls:22,vars:17,consts:[[1,"raw-data-form",3,"formGroup"],["mat-icon-button","",3,"click"],["appearance","outline"],["matInput","","type","number","formControlName","fis_id"],[4,"ngIf"],["formControlName","details"],["mat-raised-button","","color","primary",1,"raw-data-form-submit",3,"disabled","click"],["color","accent","mode","buffer",3,"value",4,"ngIf"],["color","accent","mode","buffer",3,"value"]],template:function(r,n){1&r&&(e.TgZ(0,"form",0)(1,"h2"),e._uU(2," Scrap raw data "),e.TgZ(3,"button",1),e.NdJ("click",function(){return n.openDialog()}),e.TgZ(4,"mat-icon"),e._uU(5,"help"),e.qZA()()(),e.TgZ(6,"mat-form-field",2)(7,"mat-label"),e._uU(8,"FIS ID"),e.qZA(),e._UZ(9,"input",3),e.YNc(10,Te,5,0,"mat-error",4),e.ALo(11,"hasError"),e.YNc(12,be,4,0,"mat-error",4),e.ALo(13,"hasError"),e.YNc(14,Ce,4,0,"mat-error",4),e.ALo(15,"hasError"),e.qZA(),e.TgZ(16,"mat-slide-toggle",5),e._uU(17,"Details"),e.qZA(),e.TgZ(18,"button",6),e.NdJ("click",function(){return n.submit()}),e._uU(19," Scrap! "),e.qZA()(),e.YNc(20,Ie,1,1,"mat-progress-bar",7),e.ALo(21,"async")),2&r&&(e.Q6J("formGroup",n.raceForm),e.xp6(10),e.Q6J("ngIf",e.xi3(11,6,n.fisId,"min")),e.xp6(2),e.Q6J("ngIf",e.xi3(13,9,n.fisId,"pattern")),e.xp6(2),e.Q6J("ngIf",e.xi3(15,12,n.fisId,"required")),e.xp6(4),e.Q6J("disabled",!n.raceForm.valid),e.xp6(2),e.Q6J("ngIf",e.lcZ(21,15,n.progress$)))},dependencies:[p.lW,p.RK,_.Hw,Z.Nt,l.KE,l.hX,l.TO,f.pW,b.Rr,c.O5,o._Y,o.Fj,o.wV,o.JJ,o.JL,o.sg,o.u,c.Ov,T],styles:[".raw-data-form[_ngcontent-%COMP%]{width:min(40rem,100%);padding:3rem;display:flex;gap:.5rem;flex-direction:column}.raw-data-form-submit[_ngcontent-%COMP%]{margin-top:3rem}h2[_ngcontent-%COMP%]{display:flex;align-items:center}"],changeDetection:0}),t})();var ve=i(8527);function Ue(t,a){1&t&&e._UZ(0,"app-single-race")}function Se(t,a){1&t&&e._UZ(0,"app-multi-races")}function ye(t,a){1&t&&e._UZ(0,"app-range-races")}function Fe(t,a){1&t&&e._UZ(0,"app-unprocessed-data")}function Re(t,a){1&t&&e._UZ(0,"app-scrap-table")}var C=(()=>{return(t=C||(C={})).SINGLE_RACE="SINGLE_RACE",t.MULTIPLE_RACES="MULTIPLE_RACES",t.RANGE_OF_RACES="RANGE_OF_RACES",t.RAW_DATA="RAW_DATA",t.SCRAP_TABLE="SCRAP_TABLE",C;var t})();let xe=(()=>{class t{constructor(){this.scraperTabs=C}}return t.\u0275fac=function(r){return new(r||t)},t.\u0275cmp=e.Xpm({type:t,selectors:[["app-scraper"]],decls:18,vars:15,consts:[["color","primary","backgroundColor","primary"],[3,"label"],["matTabContent",""]],template:function(r,n){1&r&&(e.TgZ(0,"mat-card")(1,"mat-tab-group",0)(2,"mat-tab",1),e.ALo(3,"capitalize"),e.YNc(4,Ue,1,0,"ng-template",2),e.qZA(),e.TgZ(5,"mat-tab",1),e.ALo(6,"capitalize"),e.YNc(7,Se,1,0,"ng-template",2),e.qZA(),e.TgZ(8,"mat-tab",1),e.ALo(9,"capitalize"),e.YNc(10,ye,1,0,"ng-template",2),e.qZA(),e.TgZ(11,"mat-tab",1),e.ALo(12,"capitalize"),e.YNc(13,Fe,1,0,"ng-template",2),e.qZA(),e.TgZ(14,"mat-tab",1),e.ALo(15,"capitalize"),e.YNc(16,Re,1,0,"ng-template",2),e.qZA()()(),e._UZ(17,"app-current-files")),2&r&&(e.xp6(2),e.Q6J("label",e.lcZ(3,5,n.scraperTabs.SINGLE_RACE)),e.xp6(3),e.Q6J("label",e.lcZ(6,7,n.scraperTabs.MULTIPLE_RACES)),e.xp6(3),e.Q6J("label",e.lcZ(9,9,n.scraperTabs.RANGE_OF_RACES)),e.xp6(3),e.Q6J("label",e.lcZ(12,11,n.scraperTabs.RAW_DATA)),e.xp6(3),e.Q6J("label",e.lcZ(15,13,n.scraperTabs.SCRAP_TABLE)))},dependencies:[d.a8,A.Vc,A.uX,A.SP,$,K,se,ue,he,Ae,ve.e],styles:["mat-card[_ngcontent-%COMP%]{margin:0 auto;width:100%;max-width:70rem}"],changeDetection:0}),t})();const Je=[{path:"",redirectTo:i(3718).$.SCRAPER.routerPath,pathMatch:"prefix"},{path:"",component:xe}];let Ee=(()=>{class t{}return t.\u0275fac=function(r){return new(r||t)},t.\u0275mod=e.oAB({type:t}),t.\u0275inj=e.cJS({imports:[S.Bz.forChild(Je),S.Bz]}),t})(),De=(()=>{class t{}return t.\u0275fac=function(r){return new(r||t)},t.\u0275mod=e.oAB({type:t}),t.\u0275inj=e.cJS({imports:[c.ez]}),t})();var qe=i(8122);let we=(()=>{class t{}return t.\u0275fac=function(r){return new(r||t)},t.\u0275mod=e.oAB({type:t}),t.\u0275inj=e.cJS({imports:[x.h,c.ez,N.t,o.u5,o.u5,o.UX,Ee,De,qe.P]}),t})()}}]);