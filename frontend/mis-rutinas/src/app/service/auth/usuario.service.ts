import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse} from "@angular/common/http";
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
// import { DatePipe } from '@angular/common';

export class Usuario {
  id:number=0;
  nombre : string="";
  apellido : string="";
  usuario : string="";
  email : string="";
  password1: string="";
  password2: string="";
  fecha : string="";
  checkbox : string="";
}

@Injectable({
  providedIn: 'root'
})

export class UsuarioService {
  url="http://127.0.0.1:8000/api/v1/registro/";

  constructor(private http:HttpClient){
    console.log("Servicio de Usuarios está corriendo...");
  }

  onCrearUsuario(usuario:Usuario):Observable<Usuario>{
    return this.http.post<Usuario>(this.url, usuario).pipe(
      catchError((error: HttpErrorResponse) => {
        console.error(error);
        return throwError(null);
      })
    );
  }
}
