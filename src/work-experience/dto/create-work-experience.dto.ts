import { IsString, IsArray, IsOptional, IsNotEmpty } from 'class-validator';

export class CreateWorkExperienceDto {
  @IsString()
  @IsNotEmpty()
  title: string;

  @IsString()
  @IsNotEmpty()
  company: string;

  @IsString()
  @IsNotEmpty()
  location: string;

  @IsString()
  @IsNotEmpty()
  startDate: string;

  @IsString()
  @IsOptional()
  endDate?: string;

  @IsArray()
  @IsString({ each: true })
  @IsNotEmpty()
  description: string[];
}
