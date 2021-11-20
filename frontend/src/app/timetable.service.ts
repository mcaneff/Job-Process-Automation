import { Injectable } from "@angular/core";
import { HttpClient, HttpHeaders, HttpErrorResponse } from "@angular/common/http";
import { observable, Observable, throwError } from "rxjs";
import { catchError} from "rxjs/operators";
import { Course, ScheduleView, ScheduleWC, TimeView,SearchView, Review, ScheduleFull, SchedList, UserProfile, ReviewAdm, Policies } from "./types";
import { Time } from '@angular/common';
import {AngularFireAuth} from '@angular/fire/auth'
import { Router } from '@angular/router';
import { stringify } from 'querystring';
const httpOptions = {
  headers: new HttpHeaders({
    "Content-Type": "application/json",
  }),
};
const httpOptionsWithAuthToken = token => ({//For authorized requests
  headers: new HttpHeaders({
    'Content-Type': 'application/json',
    'AuthToken': token,
  })
});
@Injectable({
  providedIn: "root",
})
export class TimetableService {

/**
 *This component has all the services used by different components for backend communications
 * This document does not repeat comments for similar operations. It is assumed that the reader is knowledgable enough to identify similar operations
 * .pipe() is used to pipe a request and handle errors. .subscribe() is used similarly to pass a response and error
 */
  constructor(private http: HttpClient,
    private auth: AngularFireAuth,
    private router: Router,) {}


  //Adss user to db
  createV(item): Observable<any>{
   
    return new Observable<any>(observer => {

          this.http.post<any>(
            "/api/",
            item
            ).subscribe((res) => {observer.next(res)},(error)=>{
            
            });
          })
 
    //Adss user as admin
  }

  postF(item): Observable<any>{
   
    return new Observable<any>(observer => {

          this.http.post<any>(
            "/api/",
            item
            ).subscribe((res) => {observer.next(res)},(error)=>{
            
            });
          })
 
    //Adss user as admin
  }
}